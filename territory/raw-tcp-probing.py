from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("192.168.10.15")
client.connect()

result = client.read_holding_registers(address=0, count=1)

if not result.isError():
    print(f"Current setpoint: {result.registers[0] / 10}°C")
else:
    print(result)

client.close()

