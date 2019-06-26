def recherche(nom_du_fichier, mot_a_chercher) -> list:
    """Retourne la liste des lignes qui comportent le mot donné.

    >>> recherche("../testfw/data/data.txt", "help")
    [4, 5]
    """
    lsite_des_lignes = []
    try:
        with open(nom_du_fichier, encoding='utf-8') as datafile:
            for i, ligne in enumerate(datafile):
                if mot_a_chercher in ligne:
                    lsite_des_lignes.append(i+1)
    except FileNotFoundError as msg:
        print(msg)
    return lsite_des_lignes
    
    

def inserer(tab, element, i=0, j=None) -> list:
    """Méthode dichotomique récursive.
    See also
    --------
        bisect.bisect
        bisect.insort
    Examples
    ---------
    >>> inserer([], 2)
    [2]
    >>> inserer([2], 4)
    [2, 4]
    >>> inserer([2, 4], 3)
    [2, 3, 4]
    """
    if len(tab) == 0:
        return [element]
    else:
        if j is None:
            j = len(tab)-1
        c = (i + j) // 2
        if element == tab[c]:
            # element trouvé
            return tab[:c] + [element] + tab[c:]
        elif i == j:
            # element n'est pas dans le tableau 
            if element < tab[0]:
                return [element] + tab
            elif element > tab[-1] :
                return tab + [element]
            elif element < tab[c]:
                return tab[:c] + [element] + tab[c:]
            else:
                return tab[:c+1] + [element] + tab[c+1:]
        elif element > tab[c]:
            return inserer(tab, element, i+1, j)
        else:
            return inserer(tab, element, i, j-1)

if __name__ == "__main__":
    import doctest as dt
    dt.testmod(verbose=True)

