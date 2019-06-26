## MPSI2
## AHMED AMINE ANZALI

def recherche(fichier,mot) -> list:
    fs = open(fichier,'r')
    t = []
    lignes = fichier.readlines()
    for i in range(lignes):
        if mot in ligne:
            t += i
    fs.close()
    return t
    
def inserer(tab,element) -> list:
    taille = len(tab)
    if taille == 0:
        return [element]
    else:
        a = taille//2
        if tab[a] <= element:
            return inserer(tab[:a],element)+tab[a:]
        else:
            return tab[:a+1]+inserer(tab[a+1:],element)
        
    