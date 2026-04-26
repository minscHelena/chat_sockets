import socket
import threading
import time

HOST = "0.0.0.0"
PORT = 9012

FILA_MSG = []
USERS = [] # cria uma lista de usuário para poder iterar sobre ela na hora de mandar as mensagem para todos os clientes conectados

SEMAFORO_ACESSO = threading.Semaphore(1)
SEMAFORO_ITENS = threading.Semaphore(0)

def fila_mensagens(mensagem):
    global FILA_MSG
    global SEMAFORO_ACESSO
    global SEMAFORO_ITENS

    SEMAFORO_ACESSO.acquire()
    FILA_MSG.append(mensagem)
    SEMAFORO_ACESSO.release()

    SEMAFORO_ITENS.release()

def processar_mensagens():
    global FILA_MSG
    global SEMAFORO_ACESSO
    global SEMAFORO_ITENS

    SEMAFORO_ITENS.acquire()
    SEMAFORO_ACESSO.acquire()
    if FILA_MSG:
        mensagem = FILA_MSG.pop(0)
    SEMAFORO_ACESSO.release()
    

    return mensagem


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()

        print("Servidor conectado")

        while True:
            conn, addr = s.accept() #esta aceitado conexões dos clientes

            thread = threading.Thread( #cria uma thread para cada cliente
                target=conn_cliente, #manda os dados para essa função
                args=(conn, addr),
                daemon=True
            )
            thread.start()

def conn_cliente(conn, addr):
    
    conn.sendall(b"Digite seu nome")
    data = conn.recv(1024)
    nome = data.decode('utf-8')
    USERS.append(conn) #adiciona na lista de usuário

    msg_nova_conn = f"[Servidor]: {nome} entrou no chat"
    fila_mensagens(msg_nova_conn)

    with conn:
        while True:           
            data = conn.recv(1024)
            
            if not data: #se o cliente não enviar nenhuma mensagem, ele é desconectado e removido da lista de clientes
                msg = f"[Servidor]: {nome} saiu do chat"
                fila_mensagens(msg)
                USERS.remove(conn)
                break
            
            texto = data.decode("utf-8")

            msg = f"[{nome}] ({addr[0]}) {time.strftime('%H:%M:%S')}: {texto}"

            fila_mensagens(msg)  #a cada mensagem do cliente coloca na fila
            
       


def thread_consumidora():
    while True:
        msg_consumida = processar_mensagens() #vai consumindo a fila 
        for user in USERS:
          user.sendall(msg_consumida.encode('utf-8')) #e mandando para todos os clientes

if __name__ == "__main__":
    threading.Thread(target=thread_consumidora, daemon=True).start() #criar uma thread que vai consumir a fila
    iniciar_servidor()