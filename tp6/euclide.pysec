"""
Entrée : a, b entiers (naturels)
Sortie : r entier (naturel) et  u, v entiers relatifs tels que r = pgcd(a, b) et r = a*u+b*v

Initialisation : (r, u, v, r', u', v') := (a, 1, 0, b, 0, 1)
                  q  quotient entier

les égalités r = a*u+b*v et r' = a*u'+b*v' sont des invariants de boucle

tant que (r' ≠ 0) faire
    q := r÷r' 
    (r, u, v, r', u', v') := (r', u', v', r - q *r', u - q*u', v - q*v')
    fait
renvoyer (r, u, v)
"""

def bezout(a: int, b: int) -> int:
    '''Calcule les coefficients de Bézout.
    
    '''
    (r, u, v, r_, u_, v_) = (a, 1, 0, b, 0, 1)
    while r_ != 0:
        q = r // r_
        (r, u, v, r_, u_, v_) = (r_, u_, v_, r - q *r_, u - q*u_, v - q*v_)
    return r, u, v