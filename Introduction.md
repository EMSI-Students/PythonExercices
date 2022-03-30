# C'est quoi Python
## Histoire
Python est un langage de programmation créé par Guido Van Rossum en 1989. La première version publique du langage est sortie en 1991.

![Guido Van Rossum picture from wikipedia](https://upload.wikimedia.org/wikipedia/commons/e/e2/Guido-portrait-2014-drc.jpg)

Le nom Python vient d'un hommage à la série télévisée britannique *Monty Python's Flying Circus* des années 1970, dont G. van Rossum est fan. Lorsqu'il a commencé à implémenter Python, Van Rossum a pensé qu'il lui fallait un nom court, unique et légèrement mystérieux, et a donc décidé d'appeler le langage Python.

![Monty Python's Flying Circus poster from imdb.com](https://m.media-amazon.com/images/M/MV5BOTFmYTc3ZWEtNTYxNi00OTA4LTk2NjEtNTI2MTJlNzkyMDdlXkEyXkFqcGdeQWpybA@@._V1_.jpg)

La [*Python Software Foundation (PSF)*](https://www.python.org/psf/) est une association à but non lucratif qui organise et assure la progression du langage de programmation Python, et qui anime la communauté de développeurs et d'utilisateurs.

## Caractéristiques
Ce langage de programmation présente de nombreuses caractéristiques intéressantes :

- Il est multiplateforme. C'est-à-dire qu'il fonctionne sur de nombreux systèmes d'exploitation : Windows, Mac OS X, Linux, Android, iOS, depuis les mini-ordinateurs Raspberry Pi jusqu'aux supercalculateurs.

- Il est libre (open source) et gratuit même pour les usages commerciaux. Vous pouvez l'installer sur autant d'ordinateurs que vous voulez.

- C'est un langage de haut niveau. Il demande relativement peu de connaissance sur le fonctionnement d'un ordinateur pour être utilisé.

- C'est un langage interprété. Un script Python n'a pas besoin d'être compilé pour être exécuté, contrairement à des langages comme le C ou le C++.

- Il est orienté objet. C'est-à-dire qu'il est possible de concevoir en Python des entités qui représentent celles du monde réel. Python supporte également d'autres paradigmes comme la programmation procédurale et fonctionnelle.

- Il est relativement simple à prendre en main.

- Il est trés populaire. Selon l'indice [*TIOBE*](https://www.tiobe.com/tiobe-index/) (indicateur de la popularité des langages de programmation), le langage de programmation le plus populaire en janvier/février 2022 est Python.

![Python is the most popular programming language accorging to TIOBE index](https://www.developpez.net/forums/attachments/p611299d1/a/a/a)

- Enfin, Python est un langage de programmation polyvalent qui peut être utilisé pour résoudre de nombreux problèmes, à la différence du PHP par exemple qui a clairement été imaginé pour fonctionner dans un contexte Web. Python peut être employé en développement web (côté serveur), développement de logiciels, mathématiques, analyse de données ...

    La bibliothèque standard de Python est très riche et offre un large éventail de fonctionnalités. Consultez la table des matières de la [bibliothèque standard de Python : *Python Standard Library*](https://docs.python.org/3/library/index.html#library-index) pour avoir une idée de ce qui est disponible.

# Types des langages + Compilation vs Interpretation + Procedurale vs OOP

# Python 2.x ou Python 3.x
La première grosse mise à jour de Python date de 2000 avec la version Python 2.0 Les versions se sont ensuite enchainées normalement avec Python 2.1, 2.2, 2.3, etc. jusqu'en 2008 avec la sortie de Python 3.

Python 3 a été principalement publiée pour corriger des problèmes qui existent dans Python 2, et l'équipe qui gère l'évolution du Python a fait le choix audacieux de partir sur de nouvelles bases et de casser la compatibilité avec les anciennes versions.

Python 2.x était déjà très populaire à l'époque et cela allait mettre de nombreuses personnes dans une situation délicate. L'équipe de Python a donc fait le choix de conserver deux versions du langage : Python 2.x et Python 3.x et de les faire évoluer de front.

Aujourd'hui, Python 2.7 (dernière version de 2.x) n'est plus en développement et a été abandonné en 2020.

Vous pouvez consulter l'article suivant pour en savoir plus sur la différence entre Python 2.x et Python 3.x : [Python 2 vs Python 3: What's the Difference Between Python 2.x and Python 3.x?](https://www.guru99.com/python-2-vs-python-3.html)

# Coder en Python
## Télécharger l'interpréteur Python
Python est un langage interprété, c'est-à-dire que chaque ligne de code est lue puis interprétée afin d'être exécutée par l'ordinateur. Pour coder en Python, vous avez besoin de l'interpréteur Python qui va convertir nos instructions Python en un langage compréhensible par notre ordinateur.

Il existe de nombreux autres langages interprétés comme Perl ou R. Le gros avantage de ce type de langage est qu'on peut immédiatement tester une commande à l'aide de l'interpréteur, ce qui est très utile pour débugger (c'est-à-dire trouver et corriger les éventuelles erreurs d'un programme).

L'interpréteur Python est disponible en téléchargement gratuit sur le [site officiel](https://www.python.org/downloads/) du langage.

Une fois que vous avez téléchargé la ressource Python disponible sur le site officiel, ouvrez la en double cliquant dessus. Un processus d'installation démarre. Si vous êtes sur Windows, cochez la case "Ajouter Python 3.x au PATH". Suivez ensuite le processus d'installation comme pour n'importe quel autre logiciel.

Pour exécuter nos scripts Python, il va falloir les passer à l'interpréteur. Pour cela, nous allons utiliser l'invite de commande (Windows) ou le terminal (Mac/Linux).

L'invite de commande se trouve dans le menu Démarrer de Windows sous le nom cmd. Une fois que vous êtes dans l'invite de commande ou dans le terminal, commencez par vérifier que l'interpréteur Python a bien été installé. Pour cela, tapez la commande python -V (avec un V majuscule) ou bien python --version, et pressez la touche Entrée. La version de l'interpréteur Python installée devrait vous être renvoyée.

## Ecrire du code Python
Si Python est bien été installé, nous avons deux options. On va pouvoir:
- Soit directement écrire nos instructions Python dans l'invite de commande ou dans le terminal pour les exécuter immédiatement.

- Soit créer des fichiers de script Python avec l'extension .py avec un éditeur de texte et les passer ensuite à l'interpréteur.

Ecrire son code directement dans l'invite de commande / le terminal est très pratique pour tester rapidement un code. Mais lorsque vous devrez créer de vrais programmes contenant potentiellement plusieurs scripts ou lorsque vous voudrez distribuer votre code, vous stockerez vos instructions dans des fichiers .py que vous allez créer avec un éditeur de texte ou un IDE.

### Passage par invite de commande / terminal
Ouvrez l'invite de commande / le terminal puis lancez la commande ``` python ``` pour lancer l'interpréteur Python.

Le triple chevron ```>>>``` est l'invite de commande (prompt en anglais) de l'interpréteur Python. Ici, Python attend une commande que vous devez saisir au clavier. Tapez par exemple l'instruction ```print("Hello world")```, puis validez cette commande en appuyant sur la touche Entrée.

Python a exécuté la commande directement et a affiché le texte **Hello world**. Il attend ensuite votre prochaine instruction en affichant l'invite de l'interpréteur Python (```>>>```).

Vous pouvez refaire un nouvel essai en vous servant cette fois de l'interpréteur comme d'une calculatrice :

```
>>> 1+1
2
>>> 6*3
18
```

Vous pouvez entrer une autre commande ou bien quitter l'interpréteur Python, soit en tapant la commande exit() puis en validant en appuyant sur la touche Entrée, soit en pressant simultanément les touches Ctrl et D sous Linux et Mac ou Ctrl et Z puis Entrée sous Windows.

Lorsqu'on a une longue ligne de code, on peut la couper en deux avec le caractère \ (backslash) pour des raisons de lisibilité :

```
>>> Voici une longue ligne de code \
... décrite sur deux lignes
```

Si on termine par un \\ , Python sait que la ligne de code n'est pas finie.

### Passage par IDE
Les IDE disposent de fonctionnalités supplémentaires comme des mécanismes d'auto-complétion du code ou encore de systèmes de détection des erreurs de syntaxe dans un code et de proposition de modification.

Pour ma part, dans ce cours, j'utiliserai l'IDE Visual Studio Code de Microsoft mais vous pouvez utiliser Sublime Text, Atom, ou autre. Notez par ailleurs qu'il existe certains éditeurs spécialement conçus pour écrire du code Python dont le célèbre PyCharm notamment.

![Visual Studio Code with Python from visualstudio.com](https://code.visualstudio.com/assets/docs/python/tutorial/social.png)

Vous trouverez dans [cette vidéo](https://www.youtube.com/watch?v=q8yyjhxSPdI&ab_channel=SemicolonDotDev) et [cet article](https://code.visualstudio.com/docs/python/python-tutorial) comment exécuter un code Python dans Visual Studio Code.
