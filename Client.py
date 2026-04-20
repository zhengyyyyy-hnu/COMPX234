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