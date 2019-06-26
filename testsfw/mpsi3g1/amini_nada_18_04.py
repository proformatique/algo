def recherche(nom_du_fichier, mot_a_chercher):
    t = []
    i = 0
    with open('nom_du_fichier', mode = 'r', encoding = 'utf-8') as fichier:
        for ligne in fichier.readlines():
            i += 1
            if mot_a_rechercher in ligne:
                t += [i]
    return t 
    
'''
>>> rechercher( TP13, 'tableaux')
[3,4,5,6]
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()

##

def inserer(tab,elt):
    if tab == []:
        return [elt]
    else:
        t = len(tab)//2
        t1 = tab[:t]
        t2 = tab[t:]
        if elt > tab[t]:
            return t1 + inserer(t2,elt)
        else:
            return inserer(t1,elt) + t2
'''
>>> inserer([1,3,4,5],2)
[1,2,3,4,5]
'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
##