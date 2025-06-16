import socket
import threading
# Création d'une socket côté serveur
def gerer_client(conn,addr):
    pseudo = conn.recv(1024).decode()
    print(f"Utilisateur {pseudo} connecté")
    while True:
        msg = conn.recv(1024).decode()
        if msg == "/bye":
            conn.send(f"Serveur > Au revoir {pseudo} !".encode())
            break
        else:
            conn.send(f"{pseudo} > {msg}".encode())
    conn.close()



serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("", 63001))
serveur.listen(1)
while True:
    conn, addr = serveur.accept()
    threading.Thread(target=gerer_client, args=(conn,addr)).start()


