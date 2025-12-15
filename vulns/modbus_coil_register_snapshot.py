from pymodbus.client import ModbusTcpClient

def main():
    # Create client
    client = ModbusTcpClient(host="192.168.10.15", port=502)

    with client:
        # Read 10 coils (FC01) – read-only
        coils = client.read_coils(address=0, count=10)
        if not coils.isError():
            print("Coil status:", coils.bits)

        # Read 10 holding registers (FC03) – read-only
        registers = client.read_holding_registers(address=0, count=10)
        if not registers.isError():
            print("Register values:", registers.registers)

if __name__ == "__main__":
    main()
