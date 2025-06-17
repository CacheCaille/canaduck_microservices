# canaduck_microservices

## MONCZEWSKI Gabriel
## FROISSANT Maxime


## À quel moment la socket côté serveur est-elle bloquante ?

Lorsqu'elle attend de recevoir un message.

## Que se passe-t-il si le client se connecte avant que le serveur ne soit prêt ?

Il y a une erreur "No route to host" (Errno 113).

## Quelle est la différence entre bind() et listen() ?

bind() associe la socket à une adresse et un port et listen() permet de mettre en mode serveur la socket et donc d'accepter des connexions.

## Pourquoi faut-il une boucle dans le serveur ?

Pour que le serveur puisse recevoir plusieurs message.

## Que se passe-t-il si on oublie de tester msg == "fin" ?

On sort jamais de la boucle donc le serveur ne s'arrête jamais et dans notre cas on ne peut pas accepter de nouvelles connexions.

## Est-ce que le serveur peut envoyer plusieurs réponses d’affilée ?

Non il faut qu'il attende un message d'un client pour pouvoir y répondre.

## Le serveur peut-il rester actif après une déconnexion client ?

Oui.

## Que faut-il modifier pour accepter plusieurs clients à la suite ?

Il faut enlever la gestion de la messagerie de la boucle principale et ne laisser que la gestion des connexions.

## Peut-on imaginer accepter des clients en parallèle ?

Oui, grâce aux threads.

## Comment s’assurer que les deux côtés ne parlent pas en même temps ?

Quand un côté écrit, l'autre attend, c'est possible car recv() et send() sont bloquant.

## Peut-on rendre cet échange non bloquant ? Comment ?

Oui, en créant 2 sockets, un pour lire et l'autre pour envoyer.

## Quelle est la meilleure façon de quitter proprement la communication ?

De fermer tous les sockets.

## Quels sont les risques d’utiliser eval() ? (souvenirs de FONDADEV)

eval() permet d'executer du code python.

## Comment renvoyer une erreur sans faire planter le serveur ?

En utilisant try/except.

## Pourquoi structurer les messages avec /commande ?

Afin d'avoir une sorte de standard pour le traitement des messages côté serveur.

## Comment distinguer facilement les types de messages côté serveur ?
On peut rajouter au message envoyé par le serveur un préfixe du type "Serveur > {message}"

## Que se passe-t-il si deux clients envoient des messages en même temps ?
Les clients sont sur des threads et ne partage aucune section critique donc il ne se passe rien de grave

## Peut-on garder un état partagé entre clients ? Est-ce souhaitable ?


## Que faut-il pour aller plus loin vers une vraie messagerie ?
Il faudrait que les clients voient les messages des autres clients

## Pourquoi faut-il protéger certaines sections du code ?
Pour éviter un écriture simultanée sur la ressource critique

## Que risque-t-on si deux clients modifient une même ressource simultanément ?
Sinon, deux threads peuvent écrire en même temps sur la même donnée et cela peut amener à une corruption de la donnée


