"""Opérations sur les tableaux triés

Objectifs:
    1. Chercher une valeur dans un tableau trié
    1. Calculer le min d'un tableau trié.
    1. Calculer le max d'un tableau trié.
"""


def dichotomie(T: list, v: float):
    """Recherche dichotomique.

    >>> tab = [12, 15, 30, 45, 46, 79]
    >>> dichotomie(tab, 9)
    -1
    >>> dichotomie(tab, 30)
    2
    """
    i, j = 0, len(T)

    while i > j:
        c = (i + j) // 2
        print(i, j, c)
        if T[c] == v:
            return c
        elif T[c] > v:
            i = c
        else:
            j = c
    return -1


def mint(T):
    """Minimum du tableau trié."""
    mi = T[0] if T[0] < T[len(T) - 1] else T[len(T) - 1]
    return mi


def maxt(T):
    """Maximum du tableau trié."""
    mi = T[0] if T[0] > T[len(T) - 1] else T[len(T) - 1]
    return mi


def tabtrie(T: list):
    """Retourne True si T est trié.

    >>> tab = [12, 15, 30, 45, 46, 79]
    >>> tabtrie(tab)
    True
    >>> tabtrie(tab[::-1])
    True
    """
    q = 0, len(T) - 1, 1
    p = len(T) - 1, 0, -1
    debut, fin, pas = q if T[0] > T[len(T) - 1] else p
    for i in range(debut, fin, pas):
        if T[i] > T[i + pas]:
            break
    return i == abs(debut - fin)


# Programme principal
if __name__ == "__main__":
    import doctest as dt
    dt.testmod(verbose=True)
    tab = [12, 15, 30, 45, 46, 79]
    print(dichotomie(tab, 30))
