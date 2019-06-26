'''
NOM : MOUTAWWAKIL
PRENOM : ILYAS
CLASSE : TSI
'''

def recherche(nom_du_fichier, mot_a_rechercher) -> list:
    assert type(nom_du_fichier) == type(mot_a_rechercher) == str, 'Entrée invalide !'
    try :
        f_logique = open(nom_du_fichier, mode = 'r', encoding = 'utf-8')
        i = 0
        existance = []
        for line in f_logique:# utilise moins d'espace par rapport aux autres types de parcours
            i += 1
            if mot_a_rechercher in line:
                existance += i
        f_logique.close()
        return existance
    except :
        print("Le fichier n'existe pas")
        raise FileNotFoundError