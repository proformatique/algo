# algo

[Exercice](http://conceptualmath.org/challenge/pixch/nsquare.gif)

Écrire un programme permettant de rechercher dans une matrice donnée A les éléments qui sont à la fois un maximum sur leur ligne et un minimum sur leur colonne. Ces éléments sont appelés des points-cols. Afficher les positions et les valeurs de tous les points-cols trouvés.

Écrire un programme permettant à l’utilisateur de saisir un nombre quelconque de valeurs, qui devront être stockées dans un tableau. L’utilisateur doit commencer par entrer le nombre de valeurs qu’il compte saisir. Il effectuera  ensuite cette saisie. Enfin, une fois la saisie terminée, le programme compte :

1. le nombre de valeurs négatives et de valeurs positives,
1. le nombre de valeurs paires et impaires,
1. le nombre de valeurs multiples de 3,
1. le nombre de valeurs positives, paires et multiples de 3.
Pour compter quelque chose dans un tableau, il faut utiliser… un compteur ! Le principe est simple : il consiste à initialiser une variable (qui servira de compteur) à zéro, puis parcourir le tableau grâce à une boucle (for de préférence) pour répéter un test (if) qui incrémentera le compteur seulement si la condition est vérifiée.

```math

    \sigma = \sqrt{\sum_{i=1}^n \frac{(x_i-m)^2}{n-1}}
```

Dans la suite de l'article, je noterai x la note de l'étudiant, m la moyenne originale, \sigma l'écart type original, x' la note harmonisée, m' la moyenne voulue, \sigma' l'écart type voulu.

On peut extraire x' de cette formule pour obtenir la relation qui nous intéresse :
```math

x' = \frac{\sigma'}{\sigma} (x - m) + m'.
Et voilà le travail !

```
