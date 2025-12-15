import asyncio
from asyncua import Client

async def opcua_anonymous_browse():
    client = Client("opc.tcp://192.168.20.5:4840")

    async with client:
        root = client.get_root_node()
        objects = await root.get_children()

        for obj in objects:
            name = await obj.read_browse_name()
            print(name)

if __name__ == "__main__":
    asyncio.run(opcua_anonymous_browse())
