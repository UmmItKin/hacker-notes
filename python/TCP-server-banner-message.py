import socket

def start_banner_service(host='0.0.0.0', port=31337):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Listening on {host}:{port}...")

    while True:
        # Accept a connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Send a banner message
        banner_message = "220 UmmItKin{Simple_Banner_Service}"
        client_socket.sendall(banner_message.encode('utf-8'))

        # Close the client connection
        client_socket.close()

if __name__ == "__main__":
    start_banner_service()

# to connect to the server and see the banner message, you can use:
# nc -nv 127.0.0.1 31337 
