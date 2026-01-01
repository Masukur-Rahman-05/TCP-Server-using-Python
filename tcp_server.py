import socket
import threading

class TCP_Server():
    def __init__(self,host='localhost',port=6379):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.server_socket.bind((host,port))
        self.server_socket.listen(5)
        print("Server is Listening on {host}:{port}")


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

    
    def run(self):
        try:
            while True:
                conn, addr = self.server_socket.accept()

                threading.Thread(target=self.handle_client,args=(conn,addr)).start()
        except KeyboardInterrupt:
            print("\nShutting Down the Server...")
        finally:
            self.server_socket.close()


if __name__ == "__main__":
    server = TCP_Server()
    server.run()

            


            