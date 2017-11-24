# Les tris
Les algorithmes de tri permettent d'ordonner les éléments d'un tableau.
### Activité 1
1. Tri manuel des objets par taille du plus petit au plus grand.
1. Mélanger les objets, puis répéter cette opération plusieurs fois.
1. Décrir la procédure de tri par des étapes claires.

### Activité 2
Dans le cahier d'exercices, écrire les codes des fonctions suivantes :
#### Ex. 1
##### Question 1. Définir la fonction minimumSuivant()
```python

    def minimumSuivant(T, i) -> int:
        ''' Retourne l'indice du minimum d'un tableau
            à partir d'une position i choisie.
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, position choisie
        Sorties:
        --------
            minrel : int, minimum relatif à partir de i.
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> minimumSuivant(tab, 0)
        0
        >>> minimumSuivant(tab, 2)
        3
        '''
```

##### Question 2. Définir la procédure permutater()
```python

    def premuter(T, i, j):
        ''' Permute l'élément d'indice i avec celui d'idice j dans un tableau T.
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

#### Ex. 2
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
            T : après permutation
        Exemples:
        ---------
        >>> tab = [4, 0, 5, 9, 3, 7, 8]
        >>> bonnePlace(tab, 1)
        0
        '''
```

##### Question 2. Définir la fonction cpermuter()

```python

    def cpermuter(T, i, j) -> int:
        '''Permutation circulaire entre i et j.
        Données:
        --------
            T : list, Tableau à une dimension
            i : int, indice de l'élément mal placé.
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
