def recherche(fichier, mot_a_chercher) -> list:
    a = []
    with open(fichier, encoding='utf-8') as contenu1:
        contenu = contenu1.readlines()
    for i in range(len(contenu)):
        if mot_a_chercher in contenu[i]:
            a += [i+1]
    return a

def inserer(tab, element) -> list:
    if len(tab) == 0:
        return [element]
    elif tab[len(tab)//2] < element:
        return tab[:len(tab)//2 + 1] + inserer(tab[len(tab)//2 + 1:], element)
    else:
        return inserer(tab[:len(tab)//2], element) + tab[len(tab)//2:]
