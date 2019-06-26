def recherche(nom_du_fichier, mot_a_chercher):
    with open(nom_du_fichier, 'r', encoding= 'utf_8') as df:
        index = 1
        lines = []
        for line in df:
            mots = line.split(' ')
            if mot_a_chercher in mots:
                lines+= [index]
            index+=1
    return lines
  

def inserer(tab, element):
    if len(tab) == 1 :
        if element > tab[0]:
            return [tab[0]]+[element]
        else:
            return [element]+[tab[0]]
    elif element > tab[len(tab)//2]:
        return tab[:len(tab)//2] + inserer(tab[len(tab)//2:], element)
    else:
        return inserer(tab[:len(tab)//2], element) + tab[len(tab)//2:]