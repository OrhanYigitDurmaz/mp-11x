#!/usr/bin/env python3
"""
Extract INI configuration parameters from a decompressed AudioCodes firmware image.

This script searches the raw firmware binary for parameter definition entries.
Parameters are stored as null-terminated strings in a definition table with the pattern:
  PARAM_NAME\0 description\0 [ui_label\0] [cli_path\0] [values\0]

It also finds table definitions by searching for TableName_Column patterns.

Usage:
  python3 extract_ini_params.py <firmware.bin> [output.md]

The firmware.bin should be the decompressed output from cmp_decompress.py.
"""

import re
import json
import sys
import os


def extract_strings(data):
    """Extract all null-terminated ASCII strings (3+ chars) with their offsets."""
    strings = []
    current = b''
    current_offset = 0
    for i, b in enumerate(data):
        if 32 <= b <= 126:
            if not current:
                current_offset = i
            current += bytes([b])
        else:
            if len(current) >= 3:
                strings.append((current_offset, current.decode('ascii', errors='replace').strip()))
            current = b''
    return strings


def extract_parameters(strings_list):
    """
    Find parameter definition entries (PARAM_NAME followed by description string).

    Returns dict of {name: {name, description, ui_label, cli_path, values}}.
    """
    # Match: starts with uppercase letter or digit, alphanumeric + underscore, 4+ chars
    param_re = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_]{3,}$')

    all_params = {}

    for i in range(len(strings_list) - 1):
        off1, s1 = strings_list[i]
        off2, s2 = strings_list[i + 1]

        if not s1 or not param_re.match(s1):
            continue
        if len(s1) < 4 or len(s1) > 65:
            continue
        # Skip all-lowercase short words (common English, not params)
        if s1.islower() and len(s1) < 8:
            continue

        # Check gap between strings (null padding, typically 1-20 bytes)
        actual_gap = off2 - off1 - len(s1)
        if actual_gap < 1 or actual_gap > 20:
            continue

        # s2 should be a description: has spaces, has lowercase, starts with capital/digit
        if not s2 or len(s2) < 5:
            continue
        if ' ' not in s2:
            continue
        if not any(c.islower() for c in s2):
            continue
        if not (s2[0].isupper() or s2[0].isdigit()):
            continue
        if s2.startswith('<') or s2.startswith('{') or s2.startswith('//'):
            continue

        param_name = s1
        description = s2
        values = ''
        cli_path = ''
        ui_label = ''

        # Look ahead for additional fields (ui_label, cli_path, values)
        j = i + 2
        fields_after = []
        while j < min(i + 7, len(strings_list)):
            off_j, s_j = strings_list[j]
            off_prev, s_prev = strings_list[j - 1]
            gap_j = off_j - off_prev - len(s_prev)
            if gap_j > 20:
                break
            # Check if we hit the next parameter entry
            if param_re.match(s_j) and len(s_j) >= 4:
                if j + 1 < len(strings_list):
                    _, next_next = strings_list[j + 1]
                    if next_next and ' ' in next_next and any(c.islower() for c in next_next):
                        break
            fields_after.append(s_j)
            j += 1

        for field in fields_after:
            if '/' in field and any(c.isdigit() for c in field) and ',' in field:
                if not values:
                    values = field
            elif '-' in field and len(field) < 50 and field == field.lower():
                if not cli_path:
                    cli_path = field
            elif not ui_label and field != description and len(field) > 3:
                ui_label = field

        if param_name not in all_params or len(description) > len(all_params[param_name].get('description', '')):
            all_params[param_name] = {
                'name': param_name,
                'description': description,
                'ui_label': ui_label,
                'cli_path': cli_path,
                'values': values,
            }

    return all_params


def extract_tables(data):
    """Find table definitions by searching for TableName_Column patterns."""
    col_pattern = re.compile(
        rb'([A-Za-z][A-Za-z0-9]+)_(Index|Action|ActionRes|RowStatus|[A-Z][A-Za-z0-9]+)\x00'
    )

    table_columns = {}
    for match in col_pattern.finditer(data):
        table = match.group(1).decode('ascii')
        col = match.group(2).decode('ascii')
        if col in ('Index', 'Action', 'ActionRes', 'RowStatus'):
            if table not in table_columns:
                table_columns[table] = set()
        else:
            if table not in table_columns:
                table_columns[table] = set()
            table_columns[table].add(col)

    # Validate: table must have _Index reference
    valid_tables = {}
    for match in re.finditer(rb'([A-Za-z][A-Za-z0-9]+)_Index\x00', data):
        table = match.group(1).decode('ascii')
        if table in table_columns and len(table_columns[table]) >= 1:
            valid_tables[table] = sorted(table_columns[table])

    return valid_tables


def cleanup_params(params, tables):
    """Remove entries that are clearly not INI parameters."""
    to_remove = set()
    for name, rec in params.items():
        desc = rec.get('description', '')
        # Error messages / debug strings
        if any(kw in desc for kw in ['TPNCP_TCP:', 'TPNCP_UDP:', 'task creation error',
                                       'Semaphore creation', 'FONT-SIZE:', 'Usage: PG ']):
            to_remove.add(name)
        if desc.startswith('From: VoIP') or 'column 11 is not' in desc:
            to_remove.add(name)
        if '</' in desc:
            to_remove.add(name)
        # Short ALL CAPS names with error/debug descriptions
        if len(name) == 4 and name == name.upper():
            if any(kw in desc.lower() for kw in ['error', 'failed', 'task', 'semaphore',
                                                   'font', 'usage', 'statistics', 'invalid',
                                                   'print', 'dump', 'debug']):
                to_remove.add(name)
        # Table columns already in table definitions (except ACCESSLIST which is used as scalar)
        parts = name.split('_', 1)
        if len(parts) == 2:
            table_prefix = parts[0]
            col_name = parts[1]
            if table_prefix in tables and col_name in tables[table_prefix]:
                if table_prefix not in ('ACCESSLIST',):
                    to_remove.add(name)

    for name in to_remove:
        if name in params:
            del params[name]

    return params


def generate_markdown(params, tables, source_file):
    """Generate a markdown reference document."""
    lines = []
    lines.append(f"# INI Parameters Reference")
    lines.append("")
    lines.append(f"**Source: {os.path.basename(source_file)} (reverse engineered)**")
    lines.append("")
    lines.append(f"- **Scalar parameters: {len(params)}**")
    lines.append(f"- **Table definitions: {len(tables)}**")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Scalar Parameters")
    lines.append("")
    lines.append("| # | Parameter | Description | Enumerated Values |")
    lines.append("|--:|-----------|-------------|-------------------|")

    for idx, (name, rec) in enumerate(sorted(params.items()), 1):
        desc = rec.get('description', '').replace('|', '/').replace('\n', ' ').strip()
        values = rec.get('values', '').replace('|', '/').replace('\n', ' ').strip()
        if len(desc) > 120:
            desc = desc[:117] + "..."
        if len(values) > 100:
            values = values[:97] + "..."
        lines.append(f"| {idx} | `{name}` | {desc} | {values} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Table Definitions")
    lines.append("")
    lines.append("```ini")
    lines.append("[ TableName ]")
    lines.append("FORMAT TableName_Index = TableName_Col1, TableName_Col2, ...;")
    lines.append("TableName 0 = value1, value2, ...;")
    lines.append("[ \\TableName ]")
    lines.append("```")
    lines.append("")

    for table_name in sorted(tables.keys()):
        cols = tables[table_name]
        lines.append(f"### [ {table_name} ]")
        lines.append("")
        lines.append(f"**Columns ({len(cols)}):** " + ", ".join(f"`{c}`" for c in cols))
        lines.append("")

    return '\n'.join(lines)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <firmware.bin> [output.md]")
        sys.exit(1)

    input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        base = os.path.splitext(input_path)[0]
        output_path = base + '_params.md'

    print(f"Reading: {input_path}")
    with open(input_path, 'rb') as f:
        data = f.read()
    print(f"Firmware size: {len(data)} bytes ({len(data)/1024/1024:.2f} MB)")

    print("Extracting strings...")
    strings_list = extract_strings(data)
    print(f"  Found {len(strings_list)} strings (3+ chars)")

    print("Extracting parameters...")
    params = extract_parameters(strings_list)
    print(f"  Found {len(params)} parameter definitions")

    print("Extracting table definitions...")
    tables = extract_tables(data)
    print(f"  Found {len(tables)} tables")

    print("Cleaning up...")
    params = cleanup_params(params, tables)
    print(f"  {len(params)} parameters after cleanup")

    print(f"Generating output...")
    content = generate_markdown(params, tables, input_path)
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"\nOutput: {output_path}")
    print(f"  Parameters: {len(params)}")
    print(f"  Tables: {len(tables)}")

    # Also output JSON for programmatic use
    json_path = os.path.splitext(output_path)[0] + '.json'
    with open(json_path, 'w') as f:
        json.dump({'parameters': params, 'tables': tables}, f, indent=2)
    print(f"  JSON: {json_path}")


if __name__ == '__main__':
    main()
