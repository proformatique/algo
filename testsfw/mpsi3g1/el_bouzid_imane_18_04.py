def recherche(nom_du_fichier, mot_a_chercher) :
    """
    >>> recherche('text.txt', 'a')
    [1, 6, 7]
    >>> recherche('text.txt', 'n')
    [4, 5, 6]
    """
    with open(nom_du_fichier, mode = 'r', encoding = 'utf-8') as fichier :
        texte = fichier.readlines()
    for i in range(len(texte)) :
        texte[i] = str(i+1) + texte[i]
    T = []
    for i in range(len(texte)) :
        ligne = texte[i]
        if mot_a_chercher in ligne :
            T = T + [int(ligne[0])]
    return T

def inserer(tab, element) :
    """
    >>> inserer([], 0)
    [0]
    >>> inserer([1, 2, 4], 3)
    [1, 2, 3, 4]
    """
    if len(tab) == 0 :
        return [element]
    if len(tab) == 1 :
        if element < tab[0] :
            return [element] + tab
        else :
            return tab + [element]
    else :
        c = len(tab) // 2
        if element < tab[c] :
            return inserer(tab[:c], element) + tab[c:]
        else :
            return tab[:c] + inserer(tab[c:], element)

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    
        