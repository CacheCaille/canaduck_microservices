import socket
# Création d'une socket côté serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("", 63001))
serveur.listen(1)
while True:
    conn, addr = serveur.accept()
    pseudo = conn.recv(1024).decode()
    print(f"L'utilisateur {pseudo} est connecté.")
    while True:
        message = conn.recv(1024).decode()
        parts = message.split(" ", 1)
        commande = parts[0]
        contenu = parts[1] if len(parts) > 1 else ""
        if commande == "/me":
            conn.send(f"* {pseudo} {contenu}".encode())
        elif commande == "/all":
            conn.send(f"[{pseudo}] {contenu}".encode())
        elif commande == "/bye":
            conn.send(f"À bientôt {pseudo}!".encode())
            break
        elif commande == "/help":
            conn.send("— /all <texte> : message simple à stocker. \n— /me <action> : message stylisé. \n— /bye : fermeture de session.\n — /help : commande d’aide.".encode())
    conn.close()
