def recherche(nom_du_fichier,mot_a_chercher)->list:
    with open (fichier,'r','utf_8') as h
    texte=h.read
    t=[]
    a=len(ligne)
    i=0
    cp=0
    while i < len(texte) and i>=0 :
        i+=a
        t=t.append(texte[i,i+a])
        for j in range(len(t)):
            for i in range(len(t[i])):
                if t[j][i,i+len(mot_a_chercher)]:
                    cp+=1
                else :
                    cp=cp
                return cp