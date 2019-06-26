'''Objectif : Série N° 1 : 

classe : MPSI4 G 2
Nom :
Date :
'''
# Import 
from math import sin, pi


# Defs
def et(x, y) -> bool:
    'Equiv. à and de pythin'
    xety = x == y == True # table de vérité
    return xety

def non(x) -> bool:
    'Equiv. à not de pythin'
    negx = x == False # table de vérité
    return negx
    
def ou(x, y) -> bool:
    'Equiv. à or de pythin'
    nx = non(x)
    ny = non(y)
    nxetny = et(nx, ny)
    xouy =  non(nxetny)
    return xouy

# Ex 2.1.
def f9(z):
    'Formule de la question 2.1'
    sin_pi_z = sin(pi * z)
    return sin_pi_z

def p9(z):
    '''Calculer le produit form. q2.1
    Paramters:
    ----------
        z : float
    Returns
    -------
        res : float
    '''
    prod = 1 # R.I
    n = 1 
    while True:
        ancprod = prod
        prod = prod * (1.0 - z ** 2/n ** 2) # construction
        delta = z ** 2 / n ** 2
        n += 1
        if  abs(pi * z * (ancprod - prod)) <= 1e-300:
            break
    res = prod * pi * z
    return res

# Appel / Test
a = True
b = False
print('ou(a, b) : ', ou(a, b))
print('et(a, b) : ', et(a, b))
print('non(a) : ', non(a))

z = 1/2
epsilon = 1e-3
f9z = f9(z)
p9z = p9(z)
print(f9z, p9z, abs(p9z - f9z ) < epsilon)
1.0000000016267212
1.0000000016267212








