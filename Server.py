import socket
import threading

def start_server():
    host = "zyzhshost"
    port = 51233
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server online ! ")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            # Create a thread for each client 
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, addr),
                daemon=True
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is close")
    finally:
        server_socket.close()

def handle_client(client_socket, addr):

    
