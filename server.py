import socket
# Création d'une socket côté serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("", 63001))
serveur.listen(1)
while True:
    conn, addr = serveur.accept()
    while True:
        msg = conn.recv(1024).decode()
        print("Client dit:", msg)
        if msg == "fin":
            break
        reponse = input("Répondre > ")
        conn.send(reponse.encode())
    conn.close()
serveur.close()
