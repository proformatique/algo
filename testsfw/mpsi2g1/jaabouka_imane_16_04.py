def recherche(nom_du_fichier,mot_a_chercher):
    f = open(nom_du_fichier,'r',encoding = "utf8")
    c = f.readlines()
    T = []
    n = len(mot_a_chercher) 
    for j in(len(c)):
        for i in range len(c[j]):
            if c[j][i] == mot_a_chercher[0] :
                if c[j][i:i+n] == mot_a_chercher:
                    t += [j]
    return T
def inserer(tab,elm):
    if tab ==[]:
        return [elm]
    else:
        if tab[len(tab)//2] > elm:
            return inserer(tab[0:len(tab)//2],elm)+tab[len(tab)//2:]
        else:
            return tab[0:len(tab)//2]+inserer(tab[len(tab)//2:],elm)
                


                