import asyncio
from asyncua import Client


async def test_opcua():
    client = Client("opc.tcp://192.168.50.20:4840")
    async with client:
        # Get root node
        root = client.get_root_node()
        print(f"Root: {root}")

        # Browse available objects
        objects = await root.get_children()
        for obj in objects:
            print(f"Object: {await obj.read_browse_name()}")


asyncio.run(test_opcua())
