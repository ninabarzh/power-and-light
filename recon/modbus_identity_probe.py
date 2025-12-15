from pymodbus.client import ModbusTcpClient
from pymodbus.constants import DeviceInformation

client = ModbusTcpClient(host="192.168.10.15", port=502)

if not client.connect():
    raise RuntimeError("Cannot connect")

# Read basic device identification (Function 43 / MEI 14)
response = client.read_device_information(
    read_code=DeviceInformation.BASIC
)

if response.isError():
    print("Device does not support Read Device Identification")
else:
    # Unresolved attribute reference 'information' for class 'ModbusPDU' is a type‑hint /
    # static analysis issue, not a protocol or code issue.
    for obj_id, value in response.information.items():
        print(f"{obj_id}: {value}")

client.close()
