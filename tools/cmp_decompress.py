#!/usr/bin/env python3
"""
AudioCodes MP-11x .cmp firmware decompressor.

Decompresses AudioCodes MediaPack .cmp firmware files (MP-112, MP-114, MP-118)
to raw binary images.

The .cmp format uses two-stage compression:
  1. Outer LZO: The file is split into independently LZO-compressed 128KB blocks.
     Each decompressed block contains a 64KB payload at offset 0x1042, padded with zeros.
  2. Inner LZMA: The 64KB payloads from all blocks are concatenated. Block 0 starts
     with a 13-byte LZMA header; the rest is the LZMA-compressed firmware image.

File header structure (offsets from start):
  0x00-0x03: Magic bytes: 00 4C 5A 4F (".LZO")
  0x04-0x05: Format marker: FF 1A
  0x06-0x09: Always 0x00000024 (36) for modern firmware
  0x0A-0x0B: Sub-format flag (0x0001=MP118, 0x0160=MP11X)
  0x0C-0x0D: Reserved (0x0000)
  0x0E-0x0F: Number of blocks (big-endian uint16)
  0x10-0x13: Checksum (big-endian uint32)
  0x14-0x15: Signature type (0x0008 = RSA2 present)
  0x16-0x19: "RSA2" marker
  0x1A-0x99: 128-byte RSA signature (often all zeros = unsigned)
  0x9A:      Start of LZO block data

Each LZO block:
  4 bytes: Uncompressed size (big-endian uint32, always 131072 = 128KB)
  4 bytes: Compressed size (big-endian uint32)
  N bytes: LZO1X compressed data

After LZO decompression, each 128KB block has actual payload at [0x1042:0x11042] (64KB).
Block 0 payload starts with a 13-byte LZMA header:
  Byte 0: Properties (typically 0x5D = lc=3, lp=0, pb=2)
  Bytes 1-4: Dictionary size (little-endian uint32)
  Bytes 5-12: Uncompressed size (little-endian uint64)

Usage:
  python3 cmp_decompress.py <firmware.cmp> [output.bin]
"""

import struct
import sys
import os

try:
    import lzo
except ImportError:
    sys.exit("Error: python-lzo not installed. Run: pip install python-lzo")

try:
    import lzma
except ImportError:
    sys.exit("Error: lzma module not available")


MAGIC = b'\x00LZO'
BLOCK_SIZE = 131072  # 128KB uncompressed block size
PAYLOAD_OFFSET = 0x1042  # Offset within each decompressed block where real data lives
PAYLOAD_SIZE = 0x10000  # 64KB payload per block
DATA_START = 0x9A  # Offset where LZO blocks begin in the .cmp file


def parse_header(data):
    """Parse the .cmp file header and return metadata."""
    if data[:4] != MAGIC:
        raise ValueError(f"Not a .cmp file (magic: {data[:4].hex()}, expected: {MAGIC.hex()})")

    header = {
        'magic': data[:4],
        'format_marker': data[4:6],
        'version': struct.unpack('>I', data[6:10])[0],
        'sub_format': struct.unpack('>H', data[10:12])[0],
        'reserved': struct.unpack('>H', data[12:14])[0],
        'num_blocks': struct.unpack('>H', data[14:16])[0],
        'checksum': struct.unpack('>I', data[16:20])[0],
        'sig_type': struct.unpack('>H', data[20:22])[0],
    }

    if data[22:26] == b'RSA2':
        header['has_rsa2'] = True
        header['rsa_signature'] = data[26:154]  # 128 bytes
    else:
        header['has_rsa2'] = False

    return header


def decompress_lzo_blocks(data):
    """Decompress all LZO blocks from the .cmp file. Returns list of decompressed blocks."""
    offset = DATA_START
    blocks = []

    while offset < len(data) - 8:
        uncomp_size = struct.unpack('>I', data[offset:offset+4])[0]
        comp_size = struct.unpack('>I', data[offset+4:offset+8])[0]

        if uncomp_size == 0 or comp_size == 0:
            break
        if comp_size > len(data) - offset - 8:
            break
        if uncomp_size > 1024 * 1024:
            break

        block_data = data[offset+8:offset+8+comp_size]

        if comp_size >= uncomp_size:
            decompressed = block_data[:uncomp_size]
        else:
            decompressed = lzo.decompress(block_data, False, uncomp_size)

        blocks.append(decompressed)
        offset += 8 + comp_size

    return blocks


def extract_lzma_stream(blocks):
    """
    Extract the LZMA stream from decompressed LZO blocks.

    Each block has a 64KB payload at offset 0x1042.
    Block 0's payload starts with a 13-byte LZMA header.
    """
    payloads = []
    for block in blocks:
        payload = block[PAYLOAD_OFFSET:PAYLOAD_OFFSET + PAYLOAD_SIZE]
        payloads.append(payload)

    if not payloads:
        raise ValueError("No payloads extracted from blocks")

    # Block 0 payload starts with LZMA header (13 bytes)
    lzma_header = payloads[0][:13]
    props = lzma_header[0]
    dict_size = struct.unpack('<I', lzma_header[1:5])[0]
    uncomp_size = struct.unpack('<Q', lzma_header[5:13])[0]

    lc = props % 9
    remainder = props // 9
    lp = remainder % 5
    pb = remainder // 5

    print(f"  LZMA properties: lc={lc}, lp={lp}, pb={pb}")
    print(f"  LZMA dict size: {dict_size} ({dict_size/1024/1024:.1f} MB)")
    print(f"  LZMA uncompressed size: {uncomp_size} ({uncomp_size/1024/1024:.1f} MB)")

    # Concatenate: skip 13-byte header from block 0, include all of blocks 1+
    lzma_data = payloads[0][13:]
    for payload in payloads[1:]:
        lzma_data += payload

    # Strip trailing zeros
    last_nz = len(lzma_data) - 1
    while last_nz > 0 and lzma_data[last_nz] == 0:
        last_nz -= 1
    lzma_data = lzma_data[:last_nz + 1]

    return lzma_header + lzma_data, uncomp_size


def decompress_lzma(lzma_stream, expected_size):
    """Decompress the LZMA stream."""
    return lzma.decompress(lzma_stream, format=lzma.FORMAT_ALONE)


def is_mp11x_format(blocks):
    """
    Detect whether this firmware uses the MP11X two-stage format
    (LZO blocks containing LZMA payloads at fixed offset) vs the older MP118
    format (LZO blocks are directly the firmware image).
    """
    if not blocks or len(blocks[0]) < PAYLOAD_OFFSET + 13:
        return False

    # Check if there's "ramMP118_SIP.lzma" or similar filename string
    # just before the LZMA header in block 0
    block0 = blocks[0]
    if block0[PAYLOAD_OFFSET] == 0x5D:  # LZMA properties byte
        dict_size = struct.unpack('<I', block0[PAYLOAD_OFFSET+1:PAYLOAD_OFFSET+5])[0]
        if dict_size in (1<<20, 1<<21, 1<<22, 1<<23, 1<<24):
            return True

    # Also check for the filename string pattern
    if b'.lzma' in block0[0x1000:0x1050]:
        return True

    return False


def decompress_mp118_direct(blocks):
    """For MP118 format: blocks ARE the firmware (no inner LZMA layer)."""
    return b''.join(blocks)


def decompress_cmp(filepath):
    """
    Decompress an AudioCodes .cmp firmware file.
    Returns the raw firmware binary.
    """
    with open(filepath, 'rb') as f:
        data = f.read()

    print(f"Input: {filepath}")
    print(f"File size: {len(data)} bytes")

    header = parse_header(data)
    print(f"Header:")
    print(f"  Version: {header['version']}")
    print(f"  Sub-format: 0x{header['sub_format']:04X}")
    print(f"  Blocks: {header['num_blocks']}")
    print(f"  Checksum: 0x{header['checksum']:08X}")
    print(f"  RSA2 signed: {header['has_rsa2']}")

    print(f"\nDecompressing LZO blocks...")
    blocks = decompress_lzo_blocks(data)
    print(f"  Decompressed {len(blocks)} blocks ({sum(len(b) for b in blocks)} bytes total)")

    if is_mp11x_format(blocks):
        print(f"\nDetected MP11X format (LZO + LZMA two-stage compression)")
        print(f"Extracting LZMA stream from block payloads...")
        lzma_stream, expected_size = extract_lzma_stream(blocks)
        print(f"  LZMA compressed stream: {len(lzma_stream)} bytes")

        print(f"Decompressing LZMA...")
        firmware = decompress_lzma(lzma_stream, expected_size)
        print(f"  Firmware image: {len(firmware)} bytes ({len(firmware)/1024/1024:.2f} MB)")
    else:
        print(f"\nDetected MP118 format (direct LZO blocks)")
        firmware = decompress_mp118_direct(blocks)
        print(f"  Firmware image: {len(firmware)} bytes ({len(firmware)/1024/1024:.2f} MB)")

    return firmware


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <firmware.cmp> [output.bin]")
        sys.exit(1)

    input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        base = os.path.splitext(input_path)[0]
        output_path = base + '.bin'

    firmware = decompress_cmp(input_path)

    with open(output_path, 'wb') as f:
        f.write(firmware)
    print(f"\nOutput: {output_path} ({len(firmware)} bytes)")


if __name__ == '__main__':
    main()
