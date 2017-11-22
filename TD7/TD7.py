# TD7


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
# Todo Ecrire le code


def selection(T):
    '''Parcourt T en permutant l'élément en cours T[i]
        et le minimum de T à partir de la position i.
    Permet de combiner permutation() et minimumSuivant()
    Données:
    --------
        T : list, tableau à une dimension
    Sorties:
    --------
    Exemples:
    ---------
    >>> tab = [4, 0, 5, 9, 3, 7, 8]
    >>> selection(tab)
    >>> tab
    [0, 3, 4, 5, 7, 8, 9]
    '''  # Todo Ecrire le code


'''Ecrire un programme qui permute le minimum et le premier élément
   d'un tableau à une diemension T
'''
T = [4, 8, 2, 9, 5, 7, 0]
# Todo: Ecrire le code du programme
print(T)  # doit afficher [0, 8, 2, 9, 5, 7, 4]

'''Ecrire un programme qui permute le minimum suivant et l'élément suivant
   d'un tableau à une diemension T
'''  # Todo: Ecrire le code du programme
if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
