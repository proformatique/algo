def recherche(nom_de_fichier,mot_a_chercher):
    li=[]
    cpt=1
    with open(nom_de_fichier,encoding='utf_8')as file:
        for line in file:
            if mot_a_rechercher in line:
                  li+=cpt
            cpt+=1     
        return(li) 