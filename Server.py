import socket   
import threading

host = '127.0.0.1'
port = 9090
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []
nicks = []

def main():
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor encendido...")
    connections()

# enviar el mensaje a los clientes
def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

# manejar los mensajes de cada cliente
def messages(client):
    while True:
        msg = client.recv(2048)
        broadcast(msg, client)

# se manejan las conexiones
def connections():
    while True:
        client, dir = server_socket.accept()
        client.send("nick".encode('utf-8'))
        nick = client.recv(2048).decode('utf-8')
        clients.append(client)
        nicks.append(nick)
        msg = f"{nick} conectado."
        print(msg)
        broadcast(msg.encode('utf-8'), client)
        client.send("Conectado al chat".encode('utf-8'))
        thread = threading.Thread(target = messages, args = (client,))
        thread.start()

if __name__ == '__main__':
    main()