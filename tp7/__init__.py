# -*- coding: utf-8 -*-
"""Tp7 : collections.
##############
Objectifs
-----------
    #. Utiliser les types dict, set et tuple
"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'


def myFunction(param: type) -> type:
    """Do something.

    Parameters
    ----------
    p : type
        descr
    Returns
    -------
    p : type
        descr
    See Also
    --------
    f()
    Notes
    -----
    """


## dict
"""
Que donnent les instructions suivantes?
contact = dict()
contact['nom'] = 'Ahmed'
contact['age'] = 19
contact['email'] = 'ahmed@google.com'
print(contact['email'])
contact.keys()
contact.values()
contact.items()
"""

def romain2arab(S) -> int:
    """
    Donne la valeur en chiffres arabes d'un nombre romain (en utilisant un dict)

    Examples
    --------
    >>> romain2arab('MMXVII')
    2017
    >>> romain2arab('XXXVIII')
    38
    >>> romain2arab('LXXXIII')
    83    
    >>> romain2arab('LXXXIX')
    89    
    >>> romain2arab('XCIII')
    93
    """ 
    for N in S:
        assert N.lower() in 'ivxlmdc', N + " n'est pas un chiffre valide"
    chiffres = {'M': 1000, 'D': 50, 'C':100, 'L': 50, 'X': 10, 'V': 5, 'I':1}
    S = S.upper()
    car = chiffres[S[~0]]
    sm = car
    for i in range(1, len(S)):
        ncar = chiffres[S[~i]]
        sm += -ncar if ncar < car else ncar
        car = ncar 
    return sm
    

## tuple 
"""
Que donnent les instructions suivantes:

tpl1 = 1, 2, 3
x, y, z = tpl1
tpl2 = tuple()               # Un tuple vide
tpl3 =  5,                  # Un tuple qui Comporte un élément  
print(tpl1[0])
print(tpl2)
#tpl1[0] = 5
tpl2 += tpl1
tpl2 = tpl1 * 3
# Méthodes prédéfinies
tpl2.count(1)
tpl2.index(1)
"""
# Exercices
## set
A = set('abcde')
B = {'f', 'g', 'e', 'f', 'h'}
print(A - B)        
print(A | B)
print(A ^ B)
print(A & B)
print(A >= B)
# Méthodes prédéfinies
A.difference(B)
A.union(B)
A.symmetric_difference(B)
A.intersection(B)
A.issuperset(B)
A.add(5)
A.update(B)


def poduitcartesien(x, y) -> set:
    """Retourne un ensemble set qui représente le produit cartésien de x et y.

    En mathématiques, le produit cartésien de deux ensembles X et Y, appelé ensemble-produit, est l'ensemble de tous les couples dont la première composante appartient à X et la seconde à Y.
Ecrivez une fonction qui calcule le produit cartésien.
    """

if __name__ == '__main__':
    import doctest as dt
    dt.testmod()

