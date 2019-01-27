CardsAgainstCentrale
====================

Remake du célèbre jeu Cards Against Humanity, ou de ses versions françaises Limite Limite ou Blanc Manger Coco. 
<br>
L'application est dévelopée en Python 3 avec la bibliothèque Kivy. Il s'agit d'un projet de cours.

Le jeu est jouable mais n'est pas terminé. Voir Todo plus bas pour les pistes d'améliorations. 

Utilisation
-----------

Requis : 
* Python 3
* [Kivy](https://kivy.org/#download)
* Une connexion à Internet pour jouer

Pour lancer le jeu il suffit de lancer le fichier main.py : `python main.py`<br>
Une fois le jeu lancé, il faut choisir un nom, entrer dans une partie ou en créer une si elle n'existe pas déjà.<br>
Il faut être au minimum 2 dans une partie pour pouvoir commencer. Pour tester il est possible d'ouvrir 2 instances du jeu.

Règles du jeu
-------------
Le jeu se déroule par tour. Chaque joueur dispose de 7 cartes bleues (les mots) en main. Une carte rouge (phrase) est tirée, et il faut compléter cette phrase avec un des mots en main pour effectuer la combinaison la plus drôle possible.

Une fois que tous les joueurs ont joué ou que le temps imparti est écoulé, les joueurs votent tous pour la meilleure combinaison. Le gagnant reçoit un point en cas de victoire, et personne ne reçoit de points en cas de match nul. 

La partie s'arrête lorsqu'il n'y a plus de cartes dans le jeu. 

Fonctionnement
--------------
La partie réseau s'appuie sur un serveur qui est une application web dévelopée en PHP. Celle-ci communique avec une BDD pour stocker les cartes, les joueurs et les parties. 

###Todo
* Pouvoir quitter une partie en cours. 
* Meilleure gestion des joueurs qui quittent le jeu. 
* Meilleure gestion du remplissage des parties
