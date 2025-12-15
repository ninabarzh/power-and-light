#!/usr/bin/env python3
"""
Read-only PLC program block upload (Siemens S7-300/400)
Python Snap7 1.5+, Python 3.12, Ubuntu 24.04
LAB USE ONLY
"""

import snap7

PLC_IP = "192.168.10.10"
RACK = 0
SLOT = 1

# Define protocol block type codes
BLOCK_TYPE_MAP = {'OB': 0x38, 'FC': 0x43, 'FB': 0x45, 'DB': 0x41}

plc = snap7.client.Client()
plc.connect(PLC_IP, RACK, SLOT)

if not plc.get_connected():
    raise RuntimeError("Failed to connect to PLC")

print("Connected to PLC. CPU state:", plc.get_cpu_state())

# Enumerate blocks
blocks = plc.list_blocks()

for block_name, block_numbers in [('OB', blocks.OB),
                                  ('FC', blocks.FC),
                                  ('FB', blocks.FB),
                                  ('DB', blocks.DB)]:
    block_type_code = BLOCK_TYPE_MAP[block_name]
    for block_num in block_numbers:
        data, size = plc.full_upload(block_type_code, block_num)
        filename = f"block_{block_name}_{block_num}.bin"
        with open(filename, "wb") as f:
            f.write(data)
        print(f"Dumped {filename} ({size} bytes)")

plc.disconnect()
print("Finished read-only block upload.")
