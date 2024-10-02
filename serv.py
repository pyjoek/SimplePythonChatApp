import socket
import threading

host = '127.0.0.1'
port = 1133

the = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
the.bind((host, port))

the.listen(5)

def rec(x):
    message = c.recv(1024)
    message = message.decode()

while True:
    clients, addr = the.accept()
    print(f"Got connection from {addr}")
    
    threading.Thread(target = lambda clients : clients.recv(1024).decode())

    val = input(">> ")
    clients.send(val.encode('utf-8'))
