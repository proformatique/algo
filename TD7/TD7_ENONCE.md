# Les tris
Les algorithmes de tri permettent d'ordonner les éléments d'un tableau.
### Activité 1
1. Tri manuel des objets par taille du plus petit au plus grand.
1. Mélanger les objets, puis répéter cette opération plusieurs fois.
1. Décrir la procédure de tri par des étapes claires.

### Activité 2
Dans le cahier d'exercices, écrire les codes des fonctions suivantes :
#### Ex. 1
##### Question 1. Définissez la fonction
```minimumSuivant(T, i) -> int
```
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
