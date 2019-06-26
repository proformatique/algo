'''
    Nom: Gaidi
    Prenom : EL Mehdi
    Classe: MPSI 2
    Groupe: 1
'''


def recherche(nom_du_fichier, mot_a_chercher):
    lignes = []
    cpt = 0
    with open(nom_du_fichier, encoding='utf-8') as df:
        for line in df:
            cpt += 1
            if mot_a_chercher in line:
                lignes.append(cpt)
    return lignes


def inserer(tab, element):
    if len(tab) == 0:
        return [element]
    elif tab[len(tab)//2] < element:
        return tab[:len(tab)//2 + 1] + inserer(tab[len(tab)//2 + 1:], element)
    else:
        return inserer(tab[:len(tab)//2], element) + tab[len(tab)//2:]
