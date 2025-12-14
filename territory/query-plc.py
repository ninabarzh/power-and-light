import snap7

plc = snap7.client.Client()
plc.connect('192.168.30.25', 0, 1)  # IP, rack, slot

# Read CPU status
cpu_status = plc.get_cpu_state()
print(f"PLC CPU Status: {cpu_status}")

# Read data block 1, starting at byte 0, length 100
data = plc.db_read(1, 0, 100)
print(f"Data Block 1: {data}")

plc.disconnect()
