# Les tris
Les algorithmes de tri permettent d'ordonner les éléments d'un tableau.
### Activité 1
1. Tri manuel des objets par taille du plus petit au plus grand.
1. Mélanger les objets, puis répéter cette opération plusieurs fois.
1. Décrire la procédure de tri par des étapes claires.

### Activité 2
- Dans le cahier d'exercices, écrire les codes des fonctions.
- Utiliser la machine pour tester ces fonctions.
- Exécuter les codes et corriger les erreurs de syntaxiques et sémantiques.

#### Ex. 1 Tri par sélection
Le tri par sélection (ou tri par extraction) est un algorithme de tri par comparaison.

Sur un tableau de n éléments (numérotés de 0 à n-1), le principe du tri par sélection est le suivant :

1. rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 0 ;
1. rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
1. continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.

##### Question 1. Définir la fonction minimumSuivant()
```python

    def minimumSuivant(T, i) -> int:
        ''' Retourne l'indice du minimum d'un tableau à partir d'une position i choisie.
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, position choisie
        Sorties:
        --------
            minrel : int, indice du minimum relatif à partir de i.
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> minimumSuivant(tab, 0)
        0
        >>> minimumSuivant(tab, 2)
        3
        '''
```

##### Question 2. Définir la procédure permuter()
```python

    def premuter(T, i, j):
        ''' Permute l'élément d'indice i avec celui d'indice j dans un tableau T.
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, indice du premier élément
            j : int, indice du deuxième élément
        Sorties:
        --------
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> premuter(tab, 0, 1)
        >>> tab
        [0, 4, 5, 9, 3, 7, 8]
        '''
```
##### Question 3. Définir la procédure selection()
```python

    def selection(T):
        ''' Permute l'élément d'indice i et le minimum du tableau T à partir de i.
        Données:
        --------
            T : list, Tableau à une dimension
        Sorties:
        --------
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> selection(tab)
        >>> tab
        [0, 3, 4, 5, 7, 8, 9]
        '''
```
##### Question 4. transcrire en python le pseudo-code suivant

En pseudo-code, l'algorithme s'écrit ainsi :
```
    procédure tri_selection(tableau t, entier n)
         pour i de 1 à n - 1
            min ← i
            pour j de i + 1 à n
                si t[j] < t[min], alors min ← j
            fin pour
            si min ≠ i, alors
                échanger(t[i], t[min])
            fin si
        fin pour
    fin procédure
```

#### Ex. 2 Tri par insertion
Dans l'algorithme, on parcourt le tableau à trier du début à la fin. Au moment où on considère le i-ème élément, les éléments qui le précèdent sont déjà triés. Pour faire l'analogie avec l'exemple du jeu de cartes, lorsqu'on est à la i-ème étape du parcours, le i-ème élément est la carte saisie, les éléments précédents sont la main triée et les éléments suivants correspondent aux cartes encore mélangées sur la table.

L'objectif d'une étape est d'insérer le i-ème élément à sa place parmi ceux qui précèdent. Il faut pour cela trouver où l'élément doit être inséré en le comparant aux autres, puis décaler les éléments afin de pouvoir effectuer l'insertion. En pratique, ces deux actions sont fréquemment effectuées en une passe, qui consiste à faire « remonter » l'élément au fur et à mesure jusqu'à rencontrer un élément plus petit.

##### Question 1. Définir la fonction malplace()

```python

    def malplace(T, i) -> int:
        '''Retourne l'indice de l'élément qui est plus petit que son précédent dans le tableau T à partir de i.
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, position choisie
        Sorties:
        --------
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> malplace(tab, 0)
        1
        '''
```

##### Question 2. Définir la fonction bonnePlace()

```python

    def bonnePlace(T, i) -> int:
        '''Retourne l'indice de la bonne place pour l'élément référencé par la fonction malplace().
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, indice de l'élément mal placé.
        Sorties:
        --------
            bnplace : int, position où T[i] doit être inséré.
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> bonnePlace(tab, 1)
        0
        '''
```

##### Question 3. Définir la fonction cpermuter()

```python

    def cpermuter(T, i, j) -> int:
        '''Permutation circulaire entre i et j.
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, indice de la bonne place.
            j : int, indice de l'élément mal placé.
        Sorties:
        --------
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 5, 0, 9, 3, 7, 8]
        >>> cpermuter(tab, 0, 2)
        >>> tab
        [0, 4, 5, 9, 3, 7, 8]
        '''
```
##### Question 4. transcrire en python le pseudo-code suivant
```
    procédure tri_insertion(tableau T, entier n)
       pour i de 0 à n - 1
           # mémoriser T[i] dans x
           x ← T[i]
           # décaler vers la droite les éléments de T[0]..T[i-1] qui sont plus grands que x
           j ← i
           tant que j > 0 et T[j - 1] > x
               T[j] ← T[j - 1]
               j ← j - 1
           fin tant que
           # placer x dans le "trou" que ça a laissé
           T[j] ← x
      fin pour
    fin procédure
```
#### Ex. 3 Tri à bulles
##### Question 1. Définir la fonction permutationsuccessive()

```python

    def permutationsuccessive2(T):
        '''Permutation successive conditionnée : permute uniquement les éléments successifs T[i] et T[i-1] si T[i]<T[i-1]
        Données:
        --------
            T : list, Tableau à une dimension
        Sorties:
        --------
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 5, 0, 9, 3, 7, 8]
        >>> permutationsuccessive2(tab)
        >>> tab
        [4, 0, 5, 3, 7, 8, 9]
        '''
```
##### Question 2. Définir la fonction triabulle()
```python

    def triabulle(T):
        '''Répète la permutation successive jusqu'à ce que le tableau soit trié.
        Données:
        --------
            T : list, Tableau à une dimension
        Sorties:
        --------
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 5, 0, 9, 3, 7, 8]
        >>> triabulle(tab)
        >>> tab
        [0, 3, 4, 5, 7, 8, 9]
        '''
```
##### Question 3. transcrire en python le pseudo-code suivant
Le tri à bulles ou tri par propagation est un algorithme de tri. Il consiste à comparer répétitivement les éléments consécutifs d'un tableau, et à les permuter lorsqu'ils sont mal triés. Il doit son nom au fait qu'il déplace rapidement les plus grands éléments en fin de tableau, comme des bulles d'air qui remonteraient rapidement à la surface d'un liquide.
 ```
    procédure tri_à_bulles(Tableau T)
        pour i allant de taille de T - 1 à 1
            pour j allant de 0 à i - 1
                si T[j+1] < T[j] alors
                    échanger(T[j+1], T[j])
                fin si
            fin pour
        fin pour
    fin procédure
 ```
#### Ex. 3 Mélange de Fisher-Yates
 Le mélange de Fisher-Yates, aussi appelé mélange de Knuth, est un algorithme pour générer une permutation aléatoire d'un ensemble fini, c'est-à-dire pour mélanger un ensemble d'objets.

 ##### Question 1. transcrire en python le pseudo-code suivant

 Pour mélanger un tableau T de n éléments (indicés de 0 à n-1), l'algorithme est le suivant.
```
    Pour i allant de n − 1 à 1 faire :
        j ← entier aléatoire entre 0 et i
        échanger(T[j] et T[i])
```
en python on peut générer des valeurs aléatoires en utilisant
```python

    from random import randint
    j = randint(0, 5) # 0 <= j <= 5
```
#### Ex. 4 Recherche dans un tableau trié
##### Question 1. Définir une fonction maxtri(T)
##### Question 2. Définir une fonction mintri(T)
##### Question 3. Définir une fonction recherche(T, valeur)
Il suffit de regarder si la valeur se trouve au milieu du tableau T, sinon on répète la même méthode dans la moitié gauche (resp. droite) si la valeur est plus petite  (resp.  plus grande) que l'élément au milieu.
