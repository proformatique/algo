'''
DEFAA
Fayssal
MPSI 2
'''


def recherche(nom_du_fichier, mot_a_chercher):
    L = []
    i = 0
    with open(nom_du_fichier, 'r', encoding='utf-8') as df:
        for line in df:
            i += 1
            if mot_a_chercher in line:
                L += [i]
    return L


def inserer(tab, element):
    if tab == []:
        return [element]
    else:
        n = len(tab) // 2
        if element > tab[n]:
            return tab[:n+1] + inserer(tab[n+1:], element)
        else:
            return inserer(tab[:n], element) + tab[n:]

        
                