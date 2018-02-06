import turtle as t

def koch(t, order, size):
    if order == 0:
        t.fd(size)
    else:
        koch(t, order-1, size/3)
        t.lt(60)
        koch(t, order-1, size/3)
        t.rt(120)
        koch(t, order-1, size/3)
        t.lt(60)
        koch(t, order-1, size/3)


t.up();t.goto(-300, 0); t.down()
koch(t, 4, 500)

def rfactorielle(n):
    """Ex3
    Examples
    --------
    >>> rfactorielle(0)
    1
    >>> rfactorielle(5)
    120
    """
    if n == 0:
        resultat = 1
    else:
        resultat = n * rfactorielle(n - 1)
    return resultat

def rcatalan(n):
    if n == 0:
        c = 1
    else:
        m = n - 1
        c = 2 * (2 * m + 1) / (m + 2) * rcatalan(m)
    return int(c)
    
    
    

def rpalyndrome(texte):
    if len(texte) == 0:
        resultat = True
    else:
        resultat = texte[0] == texte[len(texte)-1] and rpalyndrome(texte[1:-1])
    return resultat
    
     





