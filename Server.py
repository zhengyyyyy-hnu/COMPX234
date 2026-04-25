import socket
import threading


class read_commend:
    def __init__(self):
        self.tuples = {}

    def read(self,key):
        return self.tuples.get(key,"")

    def get(self,key):
        return self.tuples.pop(key,"")

    def put(self,key,value):
        if key not in self.tuples:
            self.tuples[key]=value
            return 0
        return 1
    
    def execute_command(self, line):
        line = line.strip()
        if not line:
           return

        parts = line.split(maxsplit=2)
        op = parts[0].upper()

        if op in ("READ", "GET"):
           if len(parts) < 2:
              return (f"ERR[{op}] ")
           k = parts[1]
           if op == "READ":
              res = self.read(k)
              return (f"OK( {k} ,'{res}')READ")
           else:
              res = self.get(k)   
              return(f"OK( {k} , '{res}')REMOVED")

        elif op == "PUT":
            if len(parts) < 3:
               print("[PUT] Error: missing key or value")
               return
            k = parts[1]
            v = parts[2]
            res = self.put(k, v)
            
            return (f"OK({k} , {v} )add")
        
        else:
             print(f"Unsupported command: {op}")

    
 

def start_server():
    host = "localhost"
    port = 51232
    
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
    try :
        command = client_socket.recv(1024).decode("utf-8")
        rc = read_commend()
        response = command + " : " + rc.execute_command( command)
        client_socket.sendall(response.encode("utf-8"))
    except Exception as e:
        print (f"Error handling client{addr}:{e}")
    finally:
        client_socket.close()
        print(f"Connection with {addr} closed")

if __name__ == "__main__":
    start_server()
        

       
    

