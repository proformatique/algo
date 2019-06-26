def recherche(nom_du_fichier , mot_a_chercher):
    file = open (nom_du_fichier , 'r' , encoding='utf-8')
    texte = file.read()
    file.close()
    my_text = texte.split('\n')
    liste = []
    for i in range(len(my_text)):
        if  mot_a_chercher in my_text[i]:
            liste.append(i+1)
    return liste