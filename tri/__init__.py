def enOrdreDecroissant(T: list):
    """Retourne True si T est en ordre décroissant.

    >>> tab = [12, 15, 30, 45, 46, 79]
    >>> enOrdreDecroissant(tab)
    False
    >>> enOrdreDecroissant(tab[::-1])
    True
    """
    ord = True
    for i in range(len(T) - 1):
        if T[i] <= T[i + 1]:
            ord = False
            break
    return ord


def enOrdreCroissant(T: list):
    """Retourne True si T est en ordre croissant.

    >>> tab = [12, 15, 30, 45, 46, 79]
    >>> enOrdreCroissant(tab)
    True
    >>> enOrdreCroissant(tab[::-1])
    False
    """
    ord = True
    for i in range(len(T) - 1):
        if T[i] >= T[i + 1]:
            ord = False
            break
    return ord


def enOrdre(T: list):
    """Retourne True si T est trié.

    >>> tab = [12, 12, 12, 12, 12, 12]
    >>> enOrdre(tab)
    True
    >>> tab = [12, 15, 30, 45, 46, 79]
    >>> enOrdre(tab)
    True
    >>> enOrdre(tab[::-1])
    True
    """
    asce = 0, len(T) - 1, 1
    desc = len(T) - 1, 0, -1
    debut, fin, pas = asce if T[0] < T[len(T) - 1] else desc
    i = debut
    while i != fin and T[i] <= T[i + pas]:
        i += pas
    return i == fin


def dichotomie(T: list, v: float):
    """Recherche dichotomique.

    Parameters
    ----------
    T : list
        Tableau à une dimension.
    v : float
        valeur à chercher.
    Returns
    -------
    ind : int
        indice de la valeur recherchée ou -1.

    Examples
    --------
    >>> tab = [12, 15, 30, 45, 46, 79]
    >>> dichotomie(tab, 9)
    -1
    >>> dichotomie(tab, 30)
    2
    """
    N = len(T)
    i, j = 0, N
    while i <= j and N > 0:
        c = (i + j) // 2
        if T[c] == v:
            return c
        elif v > T[c]:
            i = c + 1
        else:
            j = c - 1
    return -1


if __name__ == "__main__":
    import doctest as dt
    dt.testmod()
