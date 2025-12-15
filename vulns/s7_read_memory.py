import snap7

plc = snap7.client.Client()
plc.connect("192.168.10.10", 0, 1)

if not plc.get_connected():
    raise RuntimeError("Failed to connect to PLC")

# Note: python‑snap7 ships incomplete / mismatched type hints

# Read 10 bytes of inputs (PE)
inputs = plc.read_area(0x81, 0, 0, 10)

# Read 10 bytes of outputs (PA)
outputs = plc.read_area(0x82, 0, 0, 10)

# Read 100 bytes from DB1
db_data = plc.db_read(1, 0, 100)

plc.disconnect()
