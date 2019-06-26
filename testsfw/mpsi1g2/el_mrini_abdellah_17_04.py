# Abdellah Elmrini
# Mpsi1
def recherche(nom_de_fichier, mot_a_chercher):
    """
    rechercher le mot mot_a_chercher dans le fichier nom_de_fichier
    >>> recherche('testli', 'alors')
    [1, 3, 4]
    """
    l = []
    with open(nom_de_fichier, mode='r') as ndf:
        A = ndf.readlines() 
        # A est une liste dont les elements sont les lignes du fichier
        n = len(A)
        for i in range(n):
            if mot_a_chercher in A[i]:
                l += [i+1]
    return l


def inserer(tab, element):
    """
    tab est une liste triée
    on insere element dans tab par dichotomie
    test
    >>> inserer([12,54,545], 40)
    [12, 40, 54, 545]
    """
    if len(tab) == 0:
        return [element]
    if len(tab) == 1:
        if element < tab[0]:
            return [element] + tab
        else:
            return tab + [element]
    else:
        c = len(tab)//2
        tab1 = tab[:c]
        tab2 = tab[c:]
        if element < tab[c]:
            tab1 = inserer(tab1, element)
            return tab1+tab2
        else:
            tab2 = inserer(tab2, element)
            return tab1 + tab2
if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
