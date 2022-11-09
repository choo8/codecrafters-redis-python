# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client

    with conn:
        while True:
            data = conn.recv(1024)

            if data[:2] != b"*1":
                _, *client_input = data.split(" ")
                resp = f"+{' '.join(client_input)}\r\n"
            else:
                resp = b"+PONG\r\n"
            
            conn.sendall(resp)

if __name__ == "__main__":
    main()
