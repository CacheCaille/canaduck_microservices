import socket
import threading

def readServer(conn):
    lock = threading.Lock()
    while True:
        with lock:
            reponse = conn.recv(1024).decode()
            print(reponse)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("",63001))
pseudo = input()
client.send(pseudo.encode())

threading.Thread(target=readServer, args=(client,)).start()
while True:
    message = input()
    client.send(message.encode())
    if message == "/bye":
        break
client.close()
