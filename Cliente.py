import socket   
import threading

nick = input("Ingrese su nombre de usuario: ")
host = '127.0.0.1'
port = 9090
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    client_socket.connect((host, port))
    thread1 = threading.Thread(target = recv_msg)
    thread1.start()
    thread2 = threading.Thread(target = send_msg)
    thread2.start()

def recv_msg():
    while True:
        msg = client_socket.recv(2048).decode('utf-8')
        if msg == "nick":
            client_socket.send(nick.encode('utf-8'))
        else:
            print(msg)

def send_msg():
    while True:
        msg = f"{nick} > {input('')}"
        client_socket.send(msg.encode('utf-8'))

if __name__ == '__main__':
    main()