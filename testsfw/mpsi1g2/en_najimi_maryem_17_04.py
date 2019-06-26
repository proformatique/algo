def recherche(nom_du_fichier , mot_a_chercher):
    '''
        Donnes : 
            entree = nom_du_fichier, mot_a_chercher
            sortier = liste 
        >>>recherche(zoro.txt, 'oo')
        >>>
    '''
    liste = []
    with open(nom_du_fichier , encoding = 'utf-8') as fichier : 
        lignes = fichier.readlines()
        for i in range(len(lignes)):
            if mot_a_chercher in lignes[i] :
                liste += i+1
    return liste  
import doctest as dt 
dt.testmod()
def minimum(tab):
    compt = tab[0] 
    for i in range(1 ,len(tab)):
        if tab[i] < compt : 
            compt = tab[i]
    return compt
  
# test : 
if __name__ ==__'main'__: 
def trier(tab):
    tabtrie= []
    while len(tab) > 1: 
        tabtrie +=[minimum(tab)]
        tab.pop(minimum(tab))
    return tabtrie
    
def inserer(tab, element):
    
    
    
    

        
    
