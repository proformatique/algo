def recherche(nom_du_fichier, mot_a_chercher):
    """
    >>> recherche(r'C:\LYDEX\MPSI1\sami.txt', 'n')
    [1, 2]
    >>> recherche(r'C:\LYDEX\MPSI1\sami.txt', '')
    [1, 2, 3]
    """
    with open(nom_du_fichier, 'r', encoding='utf-8') as fc:
        data = fc.readlines()
    tab = []
    for i in range(len(data)):
        data[i] = str(i+1) + data[i]
    for lines in data:
        if mot_a_chercher in lines:
            tab += [int(lines[0])]
    return tab
def inserer(tab, element):
    '''
    >>> inserer( [1, 2, 4, 6], 3 )
    [1, 2, 3, 4, 6]
    >>> inserer([], 1)
    [1]
    >>> inserer([1], 1)
    [1, 1]
    >>> inserer([1], 2)
    [1, 2]
    '''
    if len(tab) == 0:
        return [element]
    if len(tab) == 1:
        if element > tab[0]:
            return tab + [element]
        else:
            return [element] + tab
    else:
        i = (len(tab)-1)//2
        if element < tab[i]:
            return  inserer(tab[:i], element) + tab[i:]
        else:
            return tab[:i] + inserer(tab[i:], element)
if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
    
    
