"""TD7 les tris.

Tableaux à une dimension
Objectifs
    Présentation et implémentation des tris de base
        - tri par séléction
        - tri par insertion
        - tri à bulles
    Réutilisation des codes
        - Faire appel aux fonctions (permutaion, permutaioncirculaire...)
        - Adapter le code d'une fonction (minimumsuivant...)
"""
# Todo : Ecrire une procédure qui permet de trier un tableau
# todo à deux dimensions M
# Todo   1) selon une colonne c tri_2d_selection(M, c)
# Todo   2) selon une ligne r tri_2d_selection2(M, r)

__author__ = 'A. MHAMEDI'
__version__ = '0.1'

import tp2.tp2_sol as tp2
# import du fichier TP2.py du Dossier TP2 sous le nom tp2
# Sous Pyzo, Il faut cocher la case "Add path to python path"
# Pyzo>>tools>>filebrowser>>star>>Add path to python path


def minimumSuivant(T, i) -> int:
    """Minimum d'un tableau.

    Retourne l'indice du minimum relatif à partir d'une position i choisie.
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
    1
    >>> minimumSuivant(tab, 2)
    4
    """
    minrel = i
    mn = T[minrel]
    for j in range(i + 1, len(T)):
        if T[j] < mn:
            minrel = j
            mn = T[minrel]
    return minrel


def selection(T):
    """Ordonner T en utilidant le tri par selection.

    Parcourt T en permutant l'élément en cours T[i] et le minimum de T
    à partir de la position i.
    Permet de combiner permutation() et minimumSuivant()
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
    """
    for i in range(len(T)):
        j = minimumSuivant(T, i)
        if i != j:  # else: pas besoin de permuter
            tp2.permutation(T, i, j)
            # on utilise la permutation déjà créée(TP2)


def selection2(T):
    """implémentation du tri par sélection."""
    for i in range(len(T) - 1):
        im = i
        for j in range(i + 1, len(T)):
            if T[j] < T[im]:
                im = j
        if im != i:
            tp2.permutation(T, i, im)


# Ex.1
# Question 1.
def malplace(T, i) -> int:
    """Retourne l'indice de l'élément mal placé.

    Qui est plus petit que son précédent dans le tableau T à partir de i.
    Donnàes:
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
    """
    assert i > 0, 'Le premier (ou l\'unique) est toujours bien placé'
    imp = i
    for j in range(i, len(T)):
        if T[j] < T[j - 1]:
            imp = j
            break
    return imp


# Question 2.
def bonnePlace(T, i) -> int:
    """Retourne l'indice de la bonne place.

    Position de l'élément référencé par la fonction malplace().
    Donnàes:
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
    """
    bnplace = i
    for j in range(i, 0, -1):
        if T[j - 1] > T[i]:
            bnplace = j - 1
    return bnplace


# Question 3.
# cette question est modifiée, on a déjà une fonction qui calcule
# la permutation nous allons l'utiliser donc, et consacrer cpermuter
# à faire toutes les permutations nécessaires pour trier le tableau
def cpermuter(T):
    """Trier T par insertion."""
    for i in range(1, len(T)):    # Parcours 1 de 1 à a
        a = malplace(T, i)        # Parcours 2 de 1 à a
        b = bonnePlace(T, a)      # Parcours 3 de a à b
        if a != b:
            tp2.permutationCirculaire(T, b, a)  # Parcours 4 de a à b
        else:
            break


# La combinaison des fonctions ne permet pas d'éviter la répétition des
# parcours, on doit combinier les codes des fonctions directement.
def tri_insertion(T):
    """Implémentation du tri par insertion."""
    for i in range(1, len(T)):
        j = i
        temp = T[j]
        while j > 0 and temp < T[j - 1]:
            T[j] = T[j - 1]
            j -= 1
        T[j] = temp


def permutationsuccessive2(T, i, j):
    """Permute les éléments successifs mal ordonnés

    parameters
    ----------
    T : list
        tableau à une dimension.
    i : int
        Indice de départ.
    j : int
        Indice de fin.
    Returns
    -------
    T : list
        permutation de T
    Examples
    --------
    >>> t = [2, 5, 3, 4]
    >>> permutationsuccessive2(t, 0, 3)
    >>> t
    [2, 3, 4, 5]
    """
    assert i < j < len(T)
    for r in range(i, j):
        if T[r] > T[r + 1]:
            T[r], T[r + 1] = T[r + 1], T[r]


def triabulle1(T):
    """Tri à bulle"""
    for j in range(len(T)):  # Est-il nécessaire de parcourir tout le tableau?
        permutationsuccessive2(T, 0, len(T))  # Opérations superflues


# Optimisation 1
def triabulle2(T):
    """Tri à bulle"""
    for j in range(len(T) - 1, 0, -1):  #
        for r in range(j):
            if T[r] > T[r + 1]:  # au passage on peut vérifier si T est trié
                T[r], T[r + 1] = T[r + 1], T[r]


# Optimisation 2
def triabulle3(T):
    """Tri à bulle"""
    for j in range(len(T) - 1, 0, -1):  #
        tritermine = True
        for r in range(j):
            if T[r] > T[r + 1]:
                T[r], T[r + 1] = T[r + 1], T[r]
                tritermine = False
        if tritermine:
            break


# PROGRAMME PRINCIPAL
if __name__ == '__main__':
    # Test automatique
    import doctest as dt
    dt.testmod(verbose=False)

    # Test manuel
    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    selection(T)
    print('Après le tri par sélection ', T)
    # doit afficher [0, 2, 4, 5, 7, 8, 9]
    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    selection2(T)
    print('Après le tri par sélection2 ', T)

    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    cpermuter(T)
    print('Aprés le tri par insertion ', T)
