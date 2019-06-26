def comptertous(n: int) -> list:
    """Compte les chiffres de n.
    
    Parameters
    ----------
    n : int
        Le nombre dont on veut compter les chiffres.
    Returns
    -------
    compteurs : list
        list des nombres des chiffres de n.

    Examples
    --------
    >>> comptertous(45)
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    >>> comptertous(115450)
    [1, 2, 0, 0, 1, 2, 0, 0, 0, 0]
    """
    compteurs = [0] * 10
    while True:
        chiffre = n % 10
        compteurs[chiffre] += 1
        n //= 10
        if n == 0:
            break
    return compteurs


def distincts(n: int) -> bool:
    """Vérifie si n est composé de chiffres distints.
    
    Parameters
    ----------
    n : int
        Le nombre à vérifier
    Returns
    -------
    dist : bool
        True si les chiffres de n sont distincts, False sinon.

    Examples
    --------
    >>> distincts(45)
    True
    >>> distincts(545)
    False
    """
    compteurs = [0] * 10
    while True:
        chiffre = n % 10
        compteurs[chiffre] += 1
        n //= 10
        if n == 0:
            break
    dist = True
    for i in range(len(compteurs)):
        if compteurs[i] > 1:
            dist = False
            break
    return dist


if __name__ == "__main__":
    import doctest as dt
    dt.testmod()
