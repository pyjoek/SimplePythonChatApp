import socket
import threading

host = '127.0.0.1'
port = 22222

the = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
the.bind((host, port))

the.listen(5)

while True:
    clients, addr = the.accept()

    while True:
        clients.send(input(":: ").encode('utf-8'))

        message = clients.recv(1024).decode('utf-8')
        print(message)
        if message == 'exit' or message == 'quit':
            break

    break
