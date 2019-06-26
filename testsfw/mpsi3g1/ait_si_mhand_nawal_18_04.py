''' NAWAL AIT SI MHAND
    MPSI 3
    GROUPE 1 '''

def rechercher(fichier,mot):
    cpt=0
    lignes=[]
    with open(fichier,mode='r',encoding= 'utf-8')as ms:
        texte= ms.read()
        return texte
    for line in texte:
        cpt+=1
        for elm in line:
            if elm == mot:
               lignes+=cpt
    return lignes
    
def inserer(tab,elm):
    p=len(tab)
    if p==0:
        tab = tab + [elm]
    else:
        if elm>tab[p-1]:
            tab = tab + [elm]
        else:
            tab = inserer(tab[:-1],elm)
    return tab                                