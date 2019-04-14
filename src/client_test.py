#!/usr/bin/env python3

import bs4
import math
import asyncio

async def tcp_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 3207)

    print("in the function")

    writer.write(message.encode())

    data = await reader.read(100)
    print("I received ", data.decode())

    print("Closed the connection")

    writer.close()

asyncio.run(tcp_client(input()))

