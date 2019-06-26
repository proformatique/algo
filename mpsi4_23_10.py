def somme2(A, B) -> list:
    '''Calcule la somme terme à terme de A et B.
    
    Parameters:
    -----------
    A : list
        Premier vecteur
    B : list
        2eme vecteur
    
    Returns
    -------
    C : list
        la somme de A + B | ci = ai + bi
    
    Examples
    --------
    >>> A = [1, 2, 3]
    >>> B = [3, 2, 1]
    >>> somme2(A, B)
    [4, 4, 4]
    
    '''
    assert len(A) == len(B), 'Données non valides!'
    # Méthode 1 : Parcourir les trois listes
    n = len(A)
    C = [None] * n
    for i in range(n):
        C[i] = A[i] + B[i]
    return C




def somme2_2(A, B):
    # Méthode 2 : MI
    C = [] # R. I
    for a, b in zip(A, B):
        C += [a + b] # Construction
    return C # R.F







def somme2_3(A, B):
    # Méthode 3 : while
    n = len(A)
    i = 0
    C = [None] * n
    while i < n:
        C[i] = A[i] + B[i]
        i += 1
    return C

def inverser(liste) -> list:
    '''Retourne une copie inversée d'une liste.
    
    Parameters:
    -----------
    liste : list
        liste de valeurs
    
    Returns
    -------
    copie : list
        copie inversée de liste
    
    Examples
    --------
    >>> inverser([1, 2, 3])
    [3, 2, 1]
    
    '''
    N = len(liste) - 1
    copie = []
    for i in range(N, -1, -1):
        copie += [liste[i]] 
    return copie


def inverser2(liste):
    # Méthode 2
    N = len(liste)
    copie = []
    for i in range(N):
        copie += [liste[- i - 1]]  # [liste[~i]]
    return copie


if __name__ == '__main__':
    import doctest as dt
    dt.testmod()

