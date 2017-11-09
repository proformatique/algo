# Les tableaux

1. Définition

    "Tableau" (array en anglais): Variable agrégeant un nombre arbitraire N de sous-variables ("composantes", "éléments") de même type

    N fonction de la "dimension" D du tableau (le nombre d'indices) et de la "taille" selon chaque indice (D tailles)

2. Remarques
    - N égal au produit des D tailles
    - Type et taille(s) spécifiés lors de la déclaration d'un tableau
    - Type et taille(s) non modifiables par la suite

# Syntaxe en langage algorithmique
## Déclaration

### Syntaxe de déclaration en dimension 1
    variables
        nomdutableau[N] : entier ;
N: Constante entière littérale ou non littérale définissant la taille selon l'unique indice
### Syntaxe de déclaration en dimension 2
    nomduTableau[N][M] : type ;
N et M: Constantes entières littérales ou non définissant les tailles (selon chacune des 2 dimensions)

### Syntaxe de déclaration en dimension D

    variables
        nomduTableau[N1][N2]...[ND] : type ;
N1, N2, ..., ND: D constantes entières littérales ou non définissant les tailles (selon chacune des n dimensions)

*ATTENTION:* Non initialisation des tableaux au moment de leur déclaration (i.e. leurs composantes ne sont pas initialisées)
## Accès aux éléments
### Syntaxe d'accès aux composantes d'un tableau de dimension 1

En lecture ou en écriture:

    variables
        nomduTableau[indice]

indice : Constante entière, variable entière ou expression à résultat entier, commençant généralement de 0.
### Syntaxe d'accès aux composantes d'un tableau de dimension 2
En lecture ou en écriture:

    nomTableau[indice1][indice2]
indice1 et indice2: Constantes entières, variables entières ou expressions à résultat entier
### Syntaxe d'accès aux composantes en dimension D
En lecture ou en écriture:

    nomTableau[i1][i2]...[iD]
i1, i2, ..., iD: Constantes entières, variables entières ou expressions à résultat entier

*"Exemples :"*
    nomTableau[0],  nomTableau[1],  nomTableau[i],  nomTableau[i+k],  nomTableau[i][k]

*"ATTENTION"*
: Pour un tableau de taille N, indices définis de 0 à N-1 et pas de 1 à N (sauf indication contraire le premier indice est toujours 0)

1. Exemple n°1: Déclaration et initialisation d'un tableau de 8 booléens avec vrai
        # Initialisation a vrai d'un tableau   de 8 booleens

        Algorithme Tableauvrai
        Variables
            tb[8] : booleen
            i : entier
        debut
            pour i de 0 à 7 faire
                tb[i] ← vrai ;
            finpour
        fin

1. Exemple n°2:
    Déclaration et initialisation d'un tableau d'entiers avec les 10 premières valeurs de n! puis affichage du contenu du tableau

        Algorithme tableau_factoriel_10
        # Initialisation d'un tableau d'entiers  avec les 10 premières valeurs du factoriel
        constante
            entier N ←10 ;
        variables
            tb[N] : entier ;
            i : entier ;
        debut
            tb[0] ← 1 ;
            pour i de 1 à N-1 faire
                tb[i] ←tb[i-1] * I;
            finpour
            pour i de 0 à N-1 faire
                ecrire(tb[i]) ;
            finpour
        fin

1. Exemple n°3: Déclaration et initialisation d'un tableau de 10x10 caractères modélisant le damier d'un jeu de dames en début de jeu:
	- Pions noirs représentés par le caractère 'N'
	- Pions blancs représentés par le caractère 'B'
	- Cases vides représentées par le caractère '.'

        Algorithme jeu
            # Initialisation d'un damier de jeu de dames
            # 'B' pour pion blanc
            # 'N' pour pion noir
            # '.' pour case vide
            # Affichage du tableau après initialisation
        variables
            damier[10][10] :caractère ;
            i,j : entier
        début
            pour i de 0 à 9 faire
                pour j de 0 à 9 faire
                    damier[i][j] ← '.' ;
                finpour
            finpour
            pour i de 0 à 8 pas 2 faire
                damier[i][0] ← 'N';
                damier[i+1][1] ← 'N';
                damier[i][2] ← 'N';
                damier[i+1][3] ← 'N';
                damier[i][9] ← 'B';
                damier[i+1][8] ← 'B';
                damier[i][7] ← 'B';
                damier[i+1][6] ← 'B'
            finpour
        fin.

# Tableau en paramètre de sous-algorithmes

1. Syntaxe

	Fonction qui prend un tableau d'entier en paramètre et retourne un tableau d'entier

		fonction mafonction (tab[] : entier, taille entier) : entier[]
		Constantes
		variables
		Début
			Retourne tab ;
		Fin

	procédure qui prend un tableau d'entier en paramètre

		procédure maprocédure (tab[] : entier, taille : entier)
		Constantes
		variables
		Début
		Fin
1. Remarques  :

    La valeur/variable passée à une fonction/procédure lors de son appel et appelé un argument

    Le passage d'argument est une affectation implicite dans laquelle le paramètre reçoit la valeur de l'argument on dit que c'est un passage par valeur.

    Parfois on a besoins de modifier l'argument lui-même, ce qui est réalisé par un passage par référence ou le paramètre et l'argument deviennent une même chose puisque ils font référence à la même variable

        X ← 8 ;
        Y ← y ;

1. Exemple :
fonction qui retourne la valeur maximal d'un tableau passé en paramètre

    fonction maxtab(tab : entier)

# En python

En python le type tableau n'existe pas dans la bibliothèque standard, pour implémenter la notion de tableau nous utiliserons le type ```list```, c'est possible d'utiliser aussi le type ```array``` de la bibliothèque array ou le type ```ndarray``` de la bibliothèque numpy.

1. Syntaxe
    ```python

        Maliste = list()    # création d'une liste vide en utilisant le constructeur list()
        MaListe = []        # création d'une liste vide en utilisant les crochets
        MaListe = [0] * 10  # Création d'une liste de dix zéros
    ```
1. Remarques
On peut :
    - Modifier la taille d'une liste : ajouter des éléments, enlever des éléments
    - mémoriser des valeurs de types différents
    - On peut même mémoriser des listes pour implémenter les tableaux multidimensionnels
    - Accéder aux éléments en utilisant des indices

# Les opérations sur les listes

## Opérateurs
```python

    L1 + L2     # concaténation
    L * 3       # répétition
    L[i]…[x]    # indices
    L[::]       # découpage
```

## Methodes
```python

    List.append(element)
    L.append(object)    # ajoute un objet à la fin
    L.count(value)      # integer – retourne le nombre d'occurrences de value
    L.extend(iterable)  # étend la liste en ajoutant des éléments à partir d'uniterable
```
## Documentation en ligne

Pour voir toutes les méthodes tapez help(list) dans la console

## Fonctions

Une liste est une séquence on peut donc appliquer la fonction ```len(liste)``` pour savoir sa taille

De même pour savoir la taille de la dimension 2 il suffit d'appeler la fonction len(liste[0])

# Passage en paramètre

En python, il n'y a pas de déclaration explicite, le passage de paramètres de type list ne change pas grand-chose dans sa définition.

Définition de fonction

```python

    def cumul(tbl) :
        N = len(tbl)
        if N > 0:
            for i in range(1, N):
                tbl[i] = tbl[i] + tbl[i - 1]
        return tbl
```
