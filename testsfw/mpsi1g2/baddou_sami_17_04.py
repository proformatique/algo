def recherche(nom_du_fichier, mot_a_rechercher)->list:
    res=[]
    with open(nom_du_fichier, encoding = "utf-8") as f:
        texte = f.read()
        a = texte.split('\n')
        for ligne in a:
            if mot_a_rechercher in ligne:
                res += ligne.index(a)
    return res
print(recherche('recherche.txt', 'world'))

