def recherche(nom_du_fichier,mot_a_rechercher) -> list:
    """Retourne les lignes qui comportent un mot donné
    >>> recherche("test.txt", "a")
    [2, 3]
    """
    with open (nom_du_fichier, encoding="utf8") as f:
        c = 0
        lst = []
        for ligne in f:
            c += 1
            if mot_a_rechercher in ligne:
                lst += [c]
        return lst
        
def inserer(tab, element)->list:
    """inserer un element dans un tableau par methode récursive
    >>> inserer([2,3,5], 5)
    [2, 3, 5, 5]
    >>> inserer([2,3,5], 4)
    [2, 3, 4, 5]
    >>> inserer([2,3,5], 3)
    [2, 3, 3, 5]
    >>> inserer([2,3,5], 2)
    [2, 2, 3, 5]
    >>> inserer([2,3,5], 1)
    [1, 2, 3, 5]
    """
    tabf = []
    n = len(tab)
    if n == 0:
        tabf = [element]
    elif n == 1:
        if tab[0] < element : 
            tabf = [tab[0],element]
        else:
            tabf = [element,tab[0]]
    else:
        if element < tab[n//2]:
            tabf =  inserer(tab[:n//2],element) + tab[n//2:]
        else:
            tabf =  tab[:(n//2)] + inserer(tab[n//2:],element) 
    return tabf

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
        
    