import socket  # noqa: F401

HOST = "localhost"
PORT = 4221


def main():
    print("Logs:")

    # Create, bind, and listen to the Server Socket:
    server_socket = socket.create_server((HOST, PORT), reuse_port=True)
    print(f"Server listening at {HOST}:{PORT}")

    try:

        # Accept incoming connections:
        conn, addr = server_socket.accept()  # wait for client
        print(f"Accepted connection from {addr}")

        # Receive data from client
        request_bytes = conn.recv(1024)
        if not request_bytes:
            print("No data received, closing connection.")
            conn.close()  # Close the client socket

        request_str = request_bytes.decode('utf-8')
        print(f"Received request from {addr}:\n{request_str[:200]}...")
        # --- Process the request and prepare the response ---
        response_body = "<h1>Hello from the server!</h1>"
        response_headers = "HTTP/1.1 200 OK\r\n"
        response_headers += "Content-Type: text/html\r\n"
        response_headers += f"Content-Length: {len(response_body.encode('utf-8'))}\r\n"
        response_headers += "Connection: close\r\n"
        response = (response_headers + "\r\n" + response_body).encode('utf-8')

        # Send the response back to the client using the NEW client_socket ('conn')
        conn.sendall(response)
        print(f"Sent response to {addr}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
