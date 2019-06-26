def recherche(fichier,mot):
    L = []
    i = 1
    with open(fichier,encoding = 'utf-8') as fic:
        M = []
        for line in fic:
            M = line.split()
            if mot in M:
                L.append(i)
            i += 1
    return L
#
def inserer(tab,element):
    if len(tab) == 0:
        return [element]
    elif len(tab) == 1:
        if element >= tab[0]:
            tab.append(element)
        else:
            tab = [element,tab[0]]
        return tab
    else:
        i = len(tab)//2
        if element == tab[i]:
            return tab[:i+1] + [element] + tab[i+1:]
        elif element > tab[i]:
            return tab[:i] + inserer(tab[i:],element)
        elif element < tab[i]: 
            return inserer(tab[:i],element) + tab[i:]
            