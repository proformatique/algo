'''Algorithmes de base : Manipulation des tableaux 1D & 2D.
A. MHAMEDI
LYDEX 2017/18
Objectifs:
    1 - Comment permuter les éléments d'un tableau?
        - Permutation de deux éléments
        - Permutation successive
        - Permutation circulaire
        - Permutation symétrique
    3 - Comment fusionner deux tableaux triés?
    4 - Manipulation des tableaux à 2 dims
'''

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

##
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
    assert 0 <= i_d < i_f < len(A) , 'Indices non valides'
    temp = A[i_f]
    for i in range(i_f, i_d, -1):
        A[i] = A[i-1]
    A[i_d] = temp

# Appel
A = [5, 2, 3, 4, 8, 9]
permutationCirculaire(A, 2, 4)
print("tableau apres permutation circulaire : ", A)   

##
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
    
A = [5, 2, 3, 4, 8, 9]
permutationSuccessive(A, 1, 4)
print(A)
    
##
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
    [9, 4, 3, 2, 8, 5]
    '''
    assert type(A) == list, ' A n\'est pas un tableau'
    N = len(A)
    for i in range(N//2):
        permutation(A, i, N-i-1)
    
A = [5, 2, 3, 4, 8, 9]
inverser(A, 1, 4)
print(A)
##
def fusion1(A, B):
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


##

def fusion2(A, B):
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
            ia += 1  # indice suivant de A
            ib += 1  # indice suivant de A
            i += 1 # Ajout d'un deuxième émlément
        elif A[ia] < B[ib]:
            F[i] = A[ia]
            ia += 1
        else:
            F[i] = B[ib]
            ib += 1
        i += 1   # indice suivant de F
    while ia < ta: # B vide ou terminé
        F[i] = A[ia]
        ia += 1
        i += 1
    while ib < tb: # A vide ou terminé
        F[i] = B[ib]
        ib += 1
        i += 1
    return F


    
    
    
    
    
    
    
    
    
    
    
    