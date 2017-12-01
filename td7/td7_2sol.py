"""Opérations sur les tableaux triés

Objectifs:
    #. Chercher une valeur dans un tableau trié
    #. Calculer le min d'un tableau trié.
    #. Calculer le max d'un tableau trié.
"""

import tp3.tp3_sol as tp3


def tri_2d_selection(M, c):
    """Trier un tableau à 2 D."""
    fin = len(M)
    for i in range(fin - 1):
        im = i
        for j in range(i + 1, fin):
            if M[j][c] < M[im][c]:
                im = j
        tp3.permuterLignes(M, i, im)


def mint(T):
    """Minimum du tableau trié."""
    mi = T[0] if T[0] < T[len(T) - 1] else T[len(T) - 1]
    return mi


def maxt(T):
    """Maximum du tableau trié."""
    mx = T[0] if T[0] > T[len(T) - 1] else T[len(T) - 1]
    return mx


# Programme principal
if __name__ == "__main__":
    import doctest as dt
    dt.testmod(report=False)
