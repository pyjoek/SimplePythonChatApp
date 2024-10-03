import socket
import threading

host = '127.0.0.1'
port = 22222

conn_2_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_2_server.connect((host, port))

while True:
    conn_2_server.send(input(">> ").encode('utf-8'))

    message = conn_2_server.recv(1024).decode('utf-8')
    print(message)
