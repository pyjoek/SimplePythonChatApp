import socket
import threading

host = '127.0.0.1'
port = 1133

conn_2_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_2_server.connect((host, port))

def rec():
    message = conn_2_server.recv(1024)
    message = message.decode('utf-8')
    print(message)

while True:
    threading.Thread(target = rec).start()

    val = input(":: ")
    conn_2_server.send(val.encode('utf-8'))
