"""TD7 les tris.
Tableaux � une dimension"""


__author__ = 'A. MHAMEDI'
__version__ = '0.1'

import TP2.TP2 as tp2
# import du fichier TP2 du Dossier TP2 sous le nom tp2
# Il faut cocher la case "Add path to python path"
# Pyzo>>tools>>filebrowser>>star>>Add path to python path


def minimumSuivant(T, i) -> int:
    ''' Retourne l'indice du minimum d'un tableau
        � partir d'une position i choisie.
    Donn�es:
    --------
        T : list, Tableau � une dimension
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
    '''
    minrel = i
    mn = T[minrel]
    for j in range(i + 1, len(T)):
        if T[j] < mn:
            minrel = j
            mn = T[minrel]
    return minrel


def selection(T):
    '''Parcourt T en permutant l'élément en cours T[i]
        et le minimum de T à partir de la position i.
    Permet de combiner permutation() et minimumSuivant()
    Données:
    --------
        T : list, Tableau � une dimension
    Sorties:
    --------
        T : apr�s permutation
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
            # on utilise la permutation d�j� cr��e(TP2)


# Ex.1
# Question 1.
def malplace(T, i) -> int:
    '''Retourne l'indice de l'�l�ment qui est plus petit
    que son pr�c�dent dans le tableau T � partir de i.
    Donn�es:
    --------
        T : list, Tableau � une dimension
        i : int, position choisie
    Sorties:
    --------
        imp : indice de l'�l�ment mal plac�
    Exemples:
    ---------
    >>> tab = [4, 0, 5, 9, 3, 7, 8]
    >>> malplace(tab, 1)
    1
    '''
    assert i > 0, 'Le premier (ou l\'unique) est toujours bien plac�'
    imp = i
    for j in range(i, len(T)):
        if T[j] < T[j - 1]:
            imp = j
            break
    return imp


# Question 2.
def bonnePlace(T, i) -> int:
    '''Retourne l'indice de la bonne place pour l'�l�ment
    r�f�renc� par la fonction malplace().
    Donn�es:
    --------
        T : list, Tableau � une dimension
        i : int, indice de l'�l�ment mal plac�.
    Sorties:
    --------
        bnplace : int, position o� T[i] doit �tre ins�r�.
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
# cette question est modifi�e, on a d�j� une fonction qui calcule
# la permutation nous allons l'utiliser donc, et consacrer cpermuter
# � faire toutes les permutations n�cessaires pour trier le tableau
def cpermuter(T):
    for i in range(1, len(T)):    # Parcours 1 de 1 � a
        a = malplace(T, i)     # Parcours 2 de 1 � a
        b = bonnePlace(T, a)   # Parcours 3 de a � b
        if a != b:
            tp2.permutationCirculaire(T, b, a)  # Parcours 4 de a � b
        else:
            break

# La combinaison des fonctions ne permet pas d'�viter la r�p�tition des
# parcours, on doit combinier les codes des fonctions directement.


if __name__ == '__main__':
    # Test automatique
    import doctest as dt
    dt.testmod(verbose=False)
    
    # Test manuel
    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    selection(T)
    print('Apr�s le tri par s�lection ', T)  # doit afficher [0, 8, 2, 9, 5, 7, 4]

    T = [4, 8, 2, 9, 5, 7, 0]
    print('Avant ', T)
    cpermuter(T)
    print('Apr�s le tri par insertion ', T)  # doit afficher [0, 8, 2, 9, 5, 7, 4]
