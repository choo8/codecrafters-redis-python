# Uncomment this to pass the first stage
import asyncio
import socket


async def handle_client(reader, writer):
    while True:
        data = await reader.read(1024)
        split_message = data.strip().split(b"\r\n")
        
        if split_message[2].lower() == b"ping":
            writer.write(b"+PONG\r\n")
        elif split_message[2].lower() == b"echo":
            print(data)
            print(split_message)
            writer.write(b"+" + split_message[-1] + b"\r\n")

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
