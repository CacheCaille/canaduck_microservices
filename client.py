import socket
# Création d'une socket côté client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.21.37", 63000))
while True:
    a_envoyer = input()
    client.send(a_envoyer.encode())
    if a_envoyer == "fin":
       break
    msg = client.recv(1024).decode()
    print("Réponse serveur :",msg)
client.close()
