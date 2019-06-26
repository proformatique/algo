

def rechercher(nom_du_fichier, mot):
    try:
        lignes = []
        compteur = 0
        with open(nom_du_fichier, mode='r', encoding ='utf-8') as f:
            for line in f:
                compteur += 1
                if mot in line:
                    lignes.append(compteur)
                return lignes
    except:
        return []
        
def inserer(tab, element):
    try:
        if len(tab)==0:
            return [element]
        else:
            if tab[len(tab)//2] > element:
                return inserer(tab[0:len(tab)//2], element) + tab[len(tab)//2:]
            else: 
                return tab[0:len(tab)//2+1] + inserer(tab[len(tab)//2+1:], element) 
    except:
        return tab
        