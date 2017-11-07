def appartient(tab, x) -> bool:
    '''teste si x fait partie de tab.
    Donnée
        tab : list tableau d'entiers
        x   : int valeur à chercher
    Sorite
        trouve : bool, True si x dans tab,
         False sinon
    Exemples
    >>> appartient([], 0)
    False
    >>> appartient([0, 5, 8], 0)
    True
    '''
    #taille = len(tab)
    #lesindices = range(taille)
    trouve = False
    for elm in tab:
        if elm == x:
            trouve = True
            break
    return trouve

def indice(tab, x) -> bool:
    '''teste si x fait partie de tab.
    Donnée
        tab : list tableau d'entiers
        x   : int valeur à chercher
    Sorite
        trouve : bool, True si x dans tab,
         False sinon
    Exemples
    >>> indice([], 0) == -1
    True
    >>> indice([0, 5, 8], 0) == 0
    True
    '''
    ind = -1 # x n'est pas trouvés
    for i, elm in enumerate(tab):
        if elm == x:
            ind = i
            break
    return ind
    
t = [1, 2, 2, 5, 2,]
x = 2
    