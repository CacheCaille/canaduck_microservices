import socket
import threading
# Création d'une socket côté serveur

connections = []
def gerer_client(conn,addr):
    lock = threading.Lock()
    pseudo = conn.recv(1024).decode()
    print(f"Utilisateur {pseudo} connecté")
    while True:
        msg = conn.recv(1024).decode()
        if msg == "/bye":
            with lock:
                for any in connections:
                    any.send(f"Serveur > Au revoir {pseudo} !".encode())
                connections.remove(conn)
                break
        else:
            with lock:
                for any in connections:
                    any.send(f"{pseudo} > {msg}".encode())
    conn.close()


serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("", 63001))
serveur.listen(1)
while True:
    conn, addr = serveur.accept()
    connections.append(conn)
    print("Clients connectés :",connections)
    threading.Thread(target=gerer_client, args=(conn,addr)).start()


