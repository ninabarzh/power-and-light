#!/usr/bin/env python3
"""
Enumerate tags from Allen-Bradley Logix PLCs using CIP.

This does NOT download ladder logic.
It provides operational visibility only.
"""

from pycomm3 import LogixDriver

PLC_IP = "192.168.10.20"

with LogixDriver(PLC_IP) as plc:
    tags = plc.get_tag_list()

    for tag in tags:
        print(f"{tag['tag_name']} : {tag['data_type']}")
