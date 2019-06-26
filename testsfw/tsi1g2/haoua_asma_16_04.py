def recherche(nom_du_fichier,mot_a_rechercher):
    with open (nom_du_fichier, 'rt', encoding='utf-8') as fichier:
        cpt,R =0,[]
        for line in fichier:
            cpt+=1
            if mot_a_rechercher in line:
                R += [cpt] 
    return R 

