'''
 TAF   : TP
 Prenom: Yassir
 Nom   : Farchi
'''

def recherche(nom_du_fichier, mot_a_chercher):
    """
    >>>recherche('text.txt', a):
    [1, 6, 9]
    T = []
    
    """
    with open(nom_du_fichier,mode = "r", encoding='uft8') as file:
        texte = file.readlines()
    for i in len(texte):
        if mot_a_chercher in texte[i]:
            T.append(i+1)
    return T

def inserer(tab, element):
    """
    >>>inserer([1, 2, 5, 9], 8)
    [1, 2, 5, 8, 9]
    
    """
    if len(tab) == 1:
        if tab[0] > element :
            tab = [element] + tab[0]
            return tab
        else:
            return tab.append(element)
    elif len(tab) == 0:
        return tab.append(element)
    else:
        m = len(tab)//2
        if tab[m] > element:
            tab = inserer(tab[:m], element) + tab[m:]
        else:
            tab = tab[:m] + inserer(tab[m:], element)
    return tab 
    
if __name__=='__main__':
    import doctest 
    doctest.testmod(verbose= True)
    