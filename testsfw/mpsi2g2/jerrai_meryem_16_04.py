def lignes(nom_de_fichier,mot_a_chercher):
    with open("n_d_f",mode='r',encoding='utf_8') as f:
        texte=f.read()
        letexte=''
        for line in texte:
          for car in line:
              if car==mot_a_chercher:
                 letexte+='\n'+line
        return letexte
    
 
def compteursep(n_d_f):
    c=0
    for car in texte :
        if car=='\n':
            c=c+1
            return c 
                 
                 
 
def rechercher(nom_de_fichier,mot_a_chercher):               
    L=[]
    for line in lignes(nom_de_fichier,mot_a_chercher):
        if car in line and car=='\n':
            L+= [compteursep(n_d_f)]
                 
                 
                 
                 
                 
         
          