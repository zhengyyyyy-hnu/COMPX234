import socket
import threading
import time

def client_task( test_number):
    # just only one client worktesk
    #"C:\Users\Administrator\Documents\GitHub\COMPX234\test-workload\client_1.txt"
    #origin textfilename
    Testfilename =rf"C:\Users\Administrator\Documents\GitHub\COMPX234\test-workload\client_{test_number}.txt"

    client_socket = None
    try :
        client_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("zyzhshost",51233))
        with open(Testfilename, "r", encoding="utf-8") as f:
            for line in f:
                  client_socket.sendall(line.strip.encode("utf-8"))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
    except Exception as e:
        print("Server is error")
    finally:
        if client_socket:
            client_socket.close()

def main():
    clients = []
    for i in range(10):
        t = threading.Thread(target=client_task, args=(i+1,))
        clients.append(t)
        t.start()
        time.sleep(0.1)
    
    for t in clients:
        t.join()
    #this part is same with your class file

if __name__ == "__main__":
    main()

    
    