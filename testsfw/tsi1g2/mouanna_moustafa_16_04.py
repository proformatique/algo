def recherche(nom_du_fichier, mot_a_rechercher) -> list :
    L = []
    i = 0
    with open (nom_du_fichier,encoding = 'utf-8') as df:
        for line in df:
            i += 1
            if mot_a_chercher in line:
                 L += [i]
        return L