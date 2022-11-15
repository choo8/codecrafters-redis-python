# Uncomment this to pass the first stage
import asyncio
import socket

redis_store = {}

async def handle_client(reader, writer):
    global redis_store

    while True:
        data = await reader.read(1024)
        split_message = data.strip().split(b"\r\n")
        
        cmd = split_message[2].lower()

        if cmd == b"ping":
            writer.write(b"+PONG\r\n")
        elif cmd == b"echo":
            writer.write(b"+" + split_message[-1] + b"\r\n")
        elif cmd == b"set":
            key, value = split_message[-3], split_message[-1]
            redis_store[key] = value
            writer.write(b"+OK\r\n")
        elif cmd == b"get":
            key = split_message[-1]
            if key in redis_store:
                writer.write(b"+" + redis_store[key] + b"\r\n")
            else:
                writer.write(b"+\r\n")

        await writer.drain()


async def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server = await asyncio.start_server(handle_client, "localhost", 6379, reuse_port=True)

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
