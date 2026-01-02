# This Code is an illustration of a Basic TCP Server using Python

```python

import socket
import threading
```

- In this part we usually import the socket module for creating socket and threading for creating thread for each connected user.
- Actually the given TCP server is Multithreaded

```python

def __init__(self,host='localhost',port=6379):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.server_socket.bind((host,port))
        self.server_socket.listen(5)
        print("Server is Listening on {host}:{port}")
```

- In this portion Server socket is defined.
- ```socket.AF_INET``` is indicating IPv4 protocol
- ```socket.SOCK_STREAM``` is indicating the data type should be in stream.
- ```setsockopt``` is indicating socket Options
- ```bind``` is actually binding the host and port together so that when any incoming response arrive the OS can decide in which port the response should go
- ```socket.SOL_SOCKET``` this is indicating socket levels
- ```socket.SO_REUSEADDR``` This will Reuse the port 
- ```1``` it will turn on the options
- ```listen(5)``` this will be listening for the incoming request and the maximum queue size will be 5. that means the further requests will be blocked


```python

def run(self):
    try:
        while True:
            conn, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client,args=(conn,addr)).start()
    except KeyboardInterrupt:
        print("\nShutting Down the Server...")
    finally:
        self.server_socket.close()

```

- In this portion the ```run()``` function Runs the server.
- ```server_socket``` accepts the request using ```accept()``` method
- This will Return two things. Connection and Address (```conn``` and  ```add```)
- Then we will assign new thread for each client using ```threading.Thread```
- This will take two arguments ```target``` and ```args```
- ```target``` will take a function ```handle_client``` that will determine what to do next after accepting a connection and ```args`` will take arguments for ```handle_client``` function
- ```KeyboardInterrupt``` will be run when user will press ```Ctrl + C```

```python

def handle_client(self,conn,addr):
        print(f"Connected by {addr}")

        try:
            while True:
                data = conn.recv(1024).encode().strip()

                if not data:
                    break
                if data.upper() == "PING":
                    conn.send(b"+PONG\r\n")
                else:
                    conn.send(b"-ERR Unknown Command\r\n")

        except Exception as e:
            conn.send(f"-ERR {e}\r\n".encode())
        finally:
            conn.close()
            print("Disconnected..{addr}")
```

- In this portion the ```handle_client``` function process the data that will be received from the connection. it will take two arguments ```conn``` and ```addr```
- The data will be received in ```1024 byte``` / ```1 KB``` using ```recv()```  method , will be encoded by ```encode()``` method
- The ```strip()``` method will remove the extra while space that has been created by ```\r\n```
- If the Client send a ```PING``` message the server will reply a ```+PONG``` message


### This is the overall idea of a basic Multithreaded TCP server using Python