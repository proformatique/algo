def recherche(nom_dufichier , mot_a_chercher) -> list:
    with open(nom_dufichier,encoding = 'utf8') as file:
        T = '' ; resultat = [] ; cpt = -1
        for line in file:
            cpt += 1
            if mot_a_chercher in line:
                resultat += [cpt]
        return resultat