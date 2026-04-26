import socket


HOST = "127.0.0.1"
PORT = 9012

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

boas_vindas = s.recv(1024).decode() 
print(boas_vindas)

nome = input("> ") 
s.sendall(nome.encode())


while True:
    mensagem = input("MSG: ")
    s.sendall(mensagem.encode())
    conf = s.recv(1024).decode()
    print(conf)