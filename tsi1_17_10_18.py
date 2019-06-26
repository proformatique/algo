'''Manipulation des listes
Définissez les focntions suivantes, remplacer pass par le code
'''
# Import 

# Ex 1 
def somme(liste) -> float:
    '''Calcule la somme des elts de liste.
    
    Parameters
    ----------
    liste : list
        liste de nombres
    Returns
    -------
    som : float
        le résultat
    Examples
    --------
    >>> somme([4, 5, -9])
    0
    >>> somme([])
    0
    
    See also
    --------
    sum()
    '''
    som = 0 # R. I.
    for elt in liste:
        som += elt # Construction
    return som # R. F.
    
# Méthode 2 à ne pas faire
def somme2(liste) -> float:    
    i = 0
    som = 0
    N = len(liste)
    while i < N:
        som += liste[i]
        i += 1
    return som
        
# Ex2
def rechercher(valeur, liste) -> int:
    '''Recherche l'indice de valeur dans liste.
    
    Parameters
    ----------
    valeur
        valeur à chercher
    liste : list
        liste de nombres

    Returns
    -------
    indice : int
        le résultat indice de la valeur, -1 sinon.

    Examples
    --------
    >>> rechercher(3, [4, 3, -9])
    1
    >>> rechercher(3, [4, [3, -9]])
    -1
    
    See also
    --------
    list.index()
    '''
    for i, elt in enumerate(liste):
        if elt == valeur:
            indice = i
            break
    else:
        indice = -1
    return indice

def rechercher2(valeur, liste):
    indice = -1
    for i, elt in enumerate(liste):
        if elt == valeur:
            indice = i
            break
    return indice

# Ex3
def compter(valeur, liste) -> int:
    ''''''
    cpt = 0
    for elt in liste:
        if elt == valeur:
            cpt += 1
    return cpt

# Ex4 min
def minimum(liste) -> float:
    '''Recherche du minimun d'une liste.
    
    Parameters
    ----------
    liste : list
        liste de nombres
    Returns
    -------
    val_min : float
        la plus petite valeur de la liste
    Examples
    --------
    >>> minimum([4, 5, -9])
    -9
    >>> minimum([1])
    1
    
    See also
    --------
    min()
    '''
    val_min = liste [0]
    for i in range(1, len(liste)):
        element = liste [i]
        if element < val_min :
            val_min = element
        # else: continue
    return val_min        
    
# Ex5 max
def maximum(liste) -> float:
    ''' Recherche du maximun d'une liste.
    
    Parameters
    ----------
    liste : list
        liste de nombres

    Returns
    -------
    val_max : float
        la plus grande valeur de la liste
    
    Examples
    --------
    >>> maximum([4, 5, -9])
    5
    >>> maximum([1])
    1
    
    See also
    --------
    max()
    '''
    val_max = liste [0]
    for i in range(1, len(liste)):
        element = liste [i]
        if element > val_max :
            val_max = element
    return val_max        
    


# Appel / Test
# Méthode 1 
assert minimum([4, 5, -9]) == -9, 'Problème !'
# Méthode 2 
if __name__ == '__main__':
    import doctest as dt
    dt.testmod()

    









