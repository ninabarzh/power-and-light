import snap7

plc = snap7.client.Client()
plc.connect('192.168.10.10', 0, 1)  # IP, rack, slot

# Check connection
cpu_state = plc.get_cpu_state()
print(f"CPU State: {cpu_state}")

# Read CPU information
cpu_info = plc.get_cpu_info()
print(f"CPU Type: {cpu_info.ModuleTypeName}")
print(f"Serial Number: {cpu_info.SerialNumber}")
print(f"Module Name: {cpu_info.ModuleName}")
