# MP-11x Firmware Reverse Engineering Tools

Tools for decompressing and extracting configuration parameters from AudioCodes
MP-11x (MP-112, MP-114, MP-118) VoIP gateway firmware files.

## Requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install python-lzo
```

Python 3.x with the `lzma` standard library module (included by default).

## Usage

### Step 1: Decompress the .cmp firmware

```bash
python3 tools/cmp_decompress.py MP11X_SIP_F6.60A.332.002.cmp firmware.bin
```

This reverse-engineers the two-stage compression (LZO + LZMA) and outputs the
raw firmware binary.

### Step 2: Extract INI parameters

```bash
python3 tools/extract_ini_params.py firmware.bin ini_parameters_reference.md
```

This searches the decompressed firmware for parameter definition entries and
produces a markdown reference and a JSON file.

### One-liner

```bash
python3 tools/cmp_decompress.py MP11X_SIP_F6.60A.332.002.cmp /tmp/fw.bin && \
python3 tools/extract_ini_params.py /tmp/fw.bin ini_parameters_reference.md
```

## .cmp File Format

### Header (0x00 - 0x99)

| Offset | Size | Description |
|--------|------|-------------|
| 0x00 | 4 | Magic: `\x00LZO` |
| 0x04 | 2 | Format marker: `\xFF\x1A` |
| 0x06 | 4 | Version (0x00000024 = 36 for modern firmware) |
| 0x0A | 2 | Sub-format (0x0001=MP118, 0x0160=MP11X) |
| 0x0C | 2 | Reserved |
| 0x0E | 2 | Number of LZO blocks (big-endian) |
| 0x10 | 4 | Checksum (big-endian) |
| 0x14 | 2 | Signature type (0x0008 = RSA2) |
| 0x16 | 4 | "RSA2" ASCII marker |
| 0x1A | 128 | RSA signature (all zeros if unsigned) |

### LZO Blocks (starting at 0x9A)

Each block:
```
[4 bytes] Uncompressed size (big-endian, always 131072 = 128KB)
[4 bytes] Compressed size (big-endian)
[N bytes] LZO1X compressed data
```

### Inner Structure (MP11X format, sub-format 0x0160)

After LZO decompression, each 128KB block contains:
- Bytes 0x0000 - 0x1041: Zero padding
- Bytes 0x1042 - 0x11041: 64KB actual payload
- Bytes 0x11042 - 0x1FFFF: Zero padding

Block 0's payload layout:
```
[13 bytes] LZMA header (props + dict_size + uncompressed_size)
[rest]     Start of LZMA compressed stream
```

Blocks 1-N continue the LZMA stream at the same offset.

The concatenated LZMA data decompresses to the full firmware image
(PowerPC VxWorks executable with embedded web interface).

### Inner Structure (MP118 format, sub-format 0x0001)

After LZO decompression, the concatenated blocks ARE the firmware image directly
(no inner LZMA layer). The firmware runs on the same PowerPC platform.

## Parameter Storage in Firmware

The decompressed firmware image contains parameter definitions as sequences of
null-terminated ASCII strings:

```
PARAMETER_NAME\0
Description text\0
UI Label\0          (optional)
cli-path-name\0     (optional)
Value1/0,Value2/1\0 (optional, enumerated values)
```

Table definitions are identified by `TableName_ColumnName` null-terminated strings
and validated by the presence of a `TableName_Index` marker.
