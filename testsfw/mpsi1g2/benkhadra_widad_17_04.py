def recherche(nom_du_fichier, mot_a_chercher):
    with open(nom_du_fichier, encoding='utf-8') as file:
        texte = file.read()
    lignes = texte.split('\n')
    resultat = []
    i = 0
    while i in len(lignes):
        if mot_a_chercher in ligne[i]:
            resultat += i+1
            i += 1
    return resultat

