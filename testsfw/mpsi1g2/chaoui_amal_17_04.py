def recherche(nom_du_fichier,mot_a_chercher) ->list:
    '''retourne une liste des indices des lignes qui comporte le mot à chercher.
    
    Donnees:
           Entrée  : nom_du_fichier(str) ,mot_a_chercher(str).
           sortie  : liste(list)
    >>> 
    
    
    ''' 
    with open(nom_du_fichier,mode='r',encoding='utf-8') as fic:
        texte=fic.read()
    liste=[]
    lignes=fic.readlines()
    nb_de_lignes=len(lignes)
    for i in range(nb_de_lignes):
        if mot_a_chercher in lignes[i]:
            liste.append(i)
    return liste        
            
import doctest as dt
dt.testmod()
           
                
