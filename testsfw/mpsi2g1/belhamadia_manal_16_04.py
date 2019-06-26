

def recherche(nom_du_fichier, mot_a_rechercher):
    i=0
    T=[]
    with open(nom_du_fichier ,encoding='utf-8') as f:
        for ligne in f:
            i+=1
            if mot_a_rechercher in ligne:
                T+=[i]
    return T



def inserer(tab,element):
    #Ã  l'aide d'une dichotomie recursive dans un tableau triÃ© selon un ordre decroissant on insere un element
    if len(tab)==0:
        tab=[element]
    else:
        if tab[len(tab)//2] <= element :
            tab=tab[: len(tab)//2+1]+inserer( tab[len(tab)//2+1:] ,element)
        else:
            tab=inserer(tab[:len(tab)//2],element)+tab[len(tab)//2  :]
    return tab
