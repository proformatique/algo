def recherche(nom_du_fichier,mot_a_chercher):
    liste=[]
    cpt=1
    with open(nom_du_fichier,encoding='utf-8') as dt:
        for line in dt:
            if mot_a_chercher in line:
                liste+=[cpt]
            cpt+=1
    return liste
