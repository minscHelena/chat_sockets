import socket

HOST = "127.0.0.1"
PORT = 9012

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.recv(1024)
s.sendall(b"Ouvinte")

while True:
        msg = s.recv(1024).decode()
        print({msg})

 

