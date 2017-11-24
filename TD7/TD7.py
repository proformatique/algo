"""TD7 les tris.
Tableaux à une dimension"""


__author__ = 'A. MHAMEDI'
__version__ = '0.1'

import TP2.TP2 as tp2
# import du fichier TP2 du Dossier TP2 sous le nom tp2
# Il faut cocher la case "Add path to python path"
# Pyzo>>tools>>filebrowser>>star>>Add path to python path


def minimumSuivant(T, i) -> int:
    ''' Retourne l'indice du minimum d'un tableau
        à partir d'une position i choisie.
    Données:
    --------
        T : list, Tableau à une dimension
        i : int, position choisie
    Sorties:
    --------
        minrel : int, indice du minimum relatif Ã  partir de i.
    Exemples:
    ---------
    >>> tab = [4, 0, 5, 9, 3, 7, 8]
    >>> minimumSuivant(tab, 0)
    1
    >>> minimumSuivant(tab, 2)
    4
    '''
    minrel = i
    mn = T[minrel]
    for j in range(i + 1, len(T)):
        if T[j] < mn:
            minrel = j
            mn = T[minrel]
    return minrel


def selection(T):
    '''Parcourt T en permutant l'Ã©lÃ©ment en cours T[i]
        et le minimum de T Ã  partir de la position i.
    Permet de combiner permutation() et minimumSuivant()
    DonnÃ©es:
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
    for i in range(len(T)):
        j = minimumSuivant(T, i)
        if i != j:  # else: pas besoin de permuter
            tp2.permutation(T, i, j)
            # on utilise la permutation déjà créée(TP2)


# Ex.1
# Question 1.
def malplace(T, i) -> int:
    '''Retourne l'indice de l'élément qui est plus petit
    que son précédent dans le tableau T à partir de i.
    Données:
    --------
        T : list, Tableau à une dimension
        i : int, position choisie
    Sorties:
    --------
        imp : indice de l'élément mal placé
    Exemples:
    ---------
    >>> tab = [4, 0, 5, 9, 3, 7, 8]
    >>> malplace(tab, 1)
    1
    '''
    assert i > 0, 'Le premier (ou l\'unique) est toujours bien placé'
    imp = i
    for j in range(i, len(T)):
        if T[j] < T[j - 1]:
            imp = j
            break
    return imp


# Question 2.
def bonnePlace(T, i) -> int:
    '''Retourne l'indice de la bonne place pour l'élément
    référencé par la fonction malplace().
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
    bnplace = i
    for j in range(i - 1, -1, -1):
        if T[i] < T[j]:
            bnplace = j
    return bnplace


# Question 3.
# cette question est modifiée, on a déjà une fonction qui calcule
# la permutation nous allons l'utiliser donc, et consacrer cpermuter
# à faire toutes les permutations nécessaires pour trier le tableau
def cpermuter(T):
    for i in range(1, len(T)):    # Parcours 1 de 1 à a
        a = malplace(T, i)     # Parcours 2 de 1 à a
        b = bonnePlace(T, a)   # Parcours 3 de a à b
        if a != b:
            tp2.permutationCirculaire(T, b, a)  # Parcours 4 de a à b
        else:
            break

# La combinaison des fonctions ne permet pas d'éviter la répétition des
# parcours, on doit combinier les codes des fonctions directement.


if __name__ == '__main__':
    # Test automatique
    import doctest as dt
    dt.testmod(verbose=False)
    
    # Test manuel
    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    selection(T)
    print('Après le tri par sélection ', T)  # doit afficher [0, 8, 2, 9, 5, 7, 4]

    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    cpermuter(T)
    print('Après le tri par insertion ', T)  # doit afficher [0, 8, 2, 9, 5, 7, 4]
