'''
Nom    : BOUISSE
Prenom : Yassir
Classe : MPSI-2
Groupe : 1
'''
def recherche(fichier, mot):
    T = []
    with open(fichier, mode='r', encoding='utf-8') as fc:
        lecture = fc.readlines()
    for i in range(len(lecture)):
        if mot in lecture[i]:
            T += [i+1]
    return T

def inserer(tab, elem):
    if len(tab) == 0:
        return [elem]
    elif tab[len(tab)//2] < elem:
        D = tab[:(len(tab)//2)+1] + inserer(tab[(len(tab)//2)+1:], elem)
        return D