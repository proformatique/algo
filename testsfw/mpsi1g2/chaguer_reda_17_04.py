def recherche(fichier, mot) -> list:
    '''
    Objectif : Fonction qui donne les indices des lignes comportant
    le mot concerné (première ligne dans le fichier est indexée par 1).
    Exemple:
    In [1]: recherche(r'C:\Users\ok\Desktop\Test.txt','en')
    Out[1]: [1, 2]
    '''
    T = []
    with open(fichier, mode='r', encoding='utf-8') as fc:
        texte = fc.readlines()
    for i in range(len(texte)):
        if mot in texte[i]:
            T += [i+1]
    return T


def inserer(tab, element) -> list:
    '''
    Objectif : Fonction qui insère dans un tableau
    trié un élément en gardant l'ordre.
    Exemple:
    In [1]: inserer([2,3,6,7,8],5)
    Out[1]: [2, 3, 5, 6, 7, 8]
    '''
    if len(tab) == 0:
        return [element]
    else:
        i = len(tab) // 2
        if tab[i] == element:
            return tab[:i]+[element] + tab[i:]
        elif tab[i] > element:
            return tab[:i] + inserer(tab[i:], element)
        else:
            return inserer(tab[:i], element) + tab[i:]

