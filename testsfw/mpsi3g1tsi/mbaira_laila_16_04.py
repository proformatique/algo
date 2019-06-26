def rechercher(nom_du_fichier,mot_a_chercher)-> list:
    tab=[]
    cpt=0
    whith open(nom_du_fichier,encoding='utf_8') as fichier:
        for ligne in fichier:
            if mot_a_chercher in ligne:
                tab += cpt
            cpt += 1
    return tab
    