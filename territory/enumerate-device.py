# The warnings "Parameter 'data' unfilled" and "Parameter 'path' unfilled" are caused by parse_operations()
# deliberately leaving fields unset until execution, and cpppo’s own type hints/validators complain even though
# the runtime fills them in later.

from cpppo.server.enip import client

host = '192.168.40.10'

with client.connector(host=host) as conn:
    # Get_Attribute_All for Identity Object (Class 0x01, Instance 1)
    ops = client.parse_operations(
        "get-attribute-all@1/1"
    )

    for index, descr, op in ops:
        conn.write(op)
        reply = conn.read()
        print("Identity object:", reply)
