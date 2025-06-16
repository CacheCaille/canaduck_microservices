import socket
# Création d'une socket côté serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("", 63001))
serveur.listen(1)
while True:
    conn, addr = serveur.accept()
    while True:
        expression = conn.recv(1024).decode()
        if expression == "fin":
            break
        print("Expression reçue: ", expression)
        try:
            result = eval(expression)
            conn.send(str(result).encode())
        except Exception as e:
            conn.send(f"Erreur: {e}".encode())
    conn.close()
