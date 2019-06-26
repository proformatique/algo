##Nom: Lefdali
##Prenom: Rida
##Classe: 1-TSI 
def recherche(nom_du_fichier, mot_a_chercher)->list:
    t = []
    cpt = 1
    with open(nom_du_fichier, encoding='UTF-8') as f:
        for ligne in f:
            if mot_a_chercher in ligne :
                t += [cpt]
            cpt += 1
        return t         
fic = 'recherche.txt'
mot = 'world'