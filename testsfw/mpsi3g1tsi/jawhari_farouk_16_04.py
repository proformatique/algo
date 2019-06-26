def recherche(nom_de_fichier,mot_a_chercher):
    try :
        list=[]
        mot = ''+mot_a_chercher+''
        cpt =1
        with open(nom_de_fichier,encoding='utf_8')as file :
            for line in file :
                if mot in line :
                    list += [cpt]
                cpt += 1
        return list
    except :
        print('File not found')

