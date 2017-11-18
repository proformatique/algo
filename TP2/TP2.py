'''Algorithmes de base : Manipulation des tableaux 1D & 2D.
A. MHAMEDI
LYDEX 2017/18
Objectifs:
    1 - Comment permuter les éléments d'un tableau?
        - Permutation de deux éléments
        - Permutation successive
        - Permutation circulaire
        - Permutation symétrique
    2 - Comment fusionner deux tableaux triés?
    3 - Manipulation des tableaux à 2 dims
'''


## DEFINITIONS
# Ex.1 Permuter deux valeurs
def permutation(A, i, j):
    '''Permet de permuter deux valeurs dans un tableau.
    Données
    -------
        A : list, tableau à une dim.
        i : int, indice de la première valeur
        j : int, indice de la 2eme valeur
    Sortie
    ------
        A : avec A[i] et A[j] échangées
    Exemple:
    >>> A = [5, 2, 3, 4, 8, 9]
    >>> permutation(A, 3, 5)
    >>> A
    [5, 2, 3, 9, 8, 4]
    '''
    assert 0 <= i < len(A) and 0 <= j < len(A), 'Indices non valides'
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    # A[i], A[j] = A[j], A[i]


# Ex.2 Permutation circulaire
def permutationCirculaire(A, i_d, i_f):
    '''Permutation circulaire entre deux indices dans un tableau.
    Données
    -------
        A : list, tableau
        i_d: int, indice de début
        i_f: int, indice de fin
    Sorities
    --------
        A : après permutation
    Exemple:
    --------
    >>> A = [5, 2, 3, 4, 8, 9]
    >>> permutationCirculaire(A, 1, 4)
    >>> A
    [5, 8, 2, 3, 4, 9]
    '''
    assert 0 <= i_d < i_f < len(A), 'Indices non valides'
    temp = A[i_f]
    for i in range(i_f, i_d, -1):
        A[i] = A[i-1]
    A[i_d] = temp


# Ex.3 Permutation successive
def permutationSuccessive(A, i_d, i_f):
    '''Permutation successive entre deux indices dans un tableau.
    Données
    -------
        A : list, tableau
        i_d: int, indice de début
        i_f: int, indice de fin
    Sorities
    --------
        A : après permutation
    Exemple:
    --------
    >>> A = [5, 2, 3, 4, 8, 9]
    >>> permutationSuccessive(A, 1, 4)
    >>> A
    [5, 3, 4, 8, 2, 9]
    '''
    assert 0 <= i_d < i_f < len(A), 'Indices non valides'
    for i in range(i_d, i_f):
        permutation(A, i, i+1)



# Ex.4 Permutation symétrique
def inverser(A):
    '''Permet d'inverser un tableau.
    Données
    -------
        A : list, tableau
     Sorities
    --------
        A : à l'envers
    Exemple:
    --------
    >>> A = [5, 2, 3, 4, 8, 9]
    >>> inverser(A)
    >>> A
    [9, 8, 4, 3, 2, 5]
    '''
    assert type(A) == list, ' A n\'est pas un tableau'
    N = len(A)
    for i in range(N//2):
        permutation(A, i, N-i-1)


# Ex.5 fusion1
def fusion1(A, B):
    '''Permet de fusionner deux tableaux triés.
    Données:
    --------
        A : list, premier tableau de taille ta
        B : list, deuxième tableau de taille tb
    Sortie:
    -------
        F : list, tableau de taille ta + tb
    '''
    assert type(A) == type(B) == list, 'A et/ou B ne sont pas des tabs.'
    ta = len(A)
    tb = len(B)
    F = [None] * (ta + tb)
    ia = 0
    ib = 0
    for i in range(len(F)):
        if ia < ta and ib < tb:
            if A[ia] < B[ib]:
                elm = A[ia]
                ia += 1
            else:
                elm = B[ib]
                ib += 1
        elif ia < ta:
            elm = A[ia]
            ia += 1
        elif ib < tb:
            elm = B[ib]
            ib += 1
        F[i] = elm
    return F


# Ex.5 fusion2
def fusion2(A, B):
    '''Permet de fusionner deux tableaux triés.
    Données:
    --------
        A : list, premier tableau de taille ta
        B : list, deuxième tableau de taille tb
    Sortie:
    -------
        F : list, tableau de taille ta + tb
    '''
    assert type(A) == type(B) == list, 'A et/ou B ne sont pas des tabs.'
    ta = len(A)
    tb = len(B)
    F = [None] * (ta + tb)  # Resultat
    ia = 0  # indice pour A
    ib = 0  # indice pour B
    i = 0   # indice pour F
    # Parcours de A et B
    while ia < ta and ib < tb:
        if A[ia] == B[ib]:
            F[i] = A[ia]
            F[i+1] = B[ib]
            ia += 1   # indice suivant de A
            ib += 1   # indice suivant de A
            i += 1    # Ajout d'un deuxième émlément
        elif A[ia] < B[ib]:
            F[i] = A[ia]
            ia += 1
        else:
            F[i] = B[ib]
            ib += 1
        i += 1      # indice suivant de F
    while ia < ta:  # B vide ou terminé
        F[i] = A[ia]
        ia += 1
        i += 1
    while ib < tb:  # A vide ou terminé
        F[i] = B[ib]
        ib += 1
        i += 1
    return F


## PROGRAMME PRINCIPAL : TEST DES PROCEDURES
# Ex.1 Permuter deux valeurs
A = [5, 2, 3, 4, 8, 9]
print("Avant la permutaion", A)
permutation(A, 3, 5)
print("Après permutation(A, 3, 5)", A)
# Ex.2 Permutation circulaire
A = [5, 2, 3, 4, 8, 9]
print("Avant la permutaion", A)
permutationCirculaire(A, 2, 4)
print("Après permutationCirculaire(A, 2, 4)", A)
# Ex.3 Permutation successive
A = [5, 2, 3, 4, 8, 9]
print("Avant la permutaion", A)
permutationSuccessive(A, 2, 4)
print("Après permutationSuccessive(A, 2, 4)", A)
# Ex.4 Permutation symétrique
A = [5, 2, 3, 4, 8, 9]
print("Avant la permutaion", A)
inverser(A)
print("Après inverser(A, 2, 4)", A)
# Ex.5 Fusion de deux tableaux triés
A = [2, 4, 7, 9, 11, 12]
B = [1, 3, 5, 6, 8, 10]
print("Avant la fusion :", A, B, sep='\n')
C = fusion1(A, B)
print("Après fusion1(A, B)", C)
C = fusion2(A, B)
print("Après fusion1(A, B)", C)
