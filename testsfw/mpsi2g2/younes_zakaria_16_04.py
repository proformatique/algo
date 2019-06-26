def recherche(fichier,mot):
    with open(fichier,encoding = 'utf-8')as df:
        L = df.readlines()
        A = []
        for i in range(len(L)):
            if mot in L[i]:
                A += [i+1]
        return A
        
def inserer(tab,elm):
    l = len(tab)
    if l == 1:
        if tab[0] <= elm:
            tab = tab + [elm]
        else:
            tab = [elm] + tab
        return tab
    if tab[l//2] < elm:
        return tab[:l//2+1]+inserer(tab[l//2 +1:],elm)
    else:
        return inserer(tab[:l//2+1],elm) + tab[l//2+1:]