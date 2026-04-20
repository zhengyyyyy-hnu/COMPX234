import socket
import threading
import time

def client_task():
    # just only one client worktesk
    client_socket = None
    try :
        client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("zyzhshost",51233))
        client_socket.sendall(Command.encode("utf-8"))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
    except Exception as e:
        print("Server is error")
    finally:
        if client_socket:
            client_socket.close()
    
    