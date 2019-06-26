def recherche(nom_du_fichier,mot_a_chercher) -> list:
    """Retourne une liste d'indices des lignes qui comporte un mot donné.
    >>> recherche('fichier_test.docx','mot'):
    [1,3,5]
    """
    f = open(nom_du_fichier, 'r' , encoding= 'utf-8')
    liste = []          #liste a retourner 
    i = 0               #liste de lignes
    for ligne in f.readline():
        i=+1
        if mot_a_rechercher in ligne:
            liste += [i]
    return liste 
    
def inserer(tab,element) -> list:
    """retourne un tableau trié aprés l'ajout d'un element donné.
    >>> inserer([1, 3, 4, 5],2) 
    [1,2,3,4,5]
    """
    T=[]
    n=len(tab)//2
    if tab==[]:
        T=[element]
    elif tab[n]<element:
        T=tab[:n+1]+inserer(tab[n+1:],element)
    else:
        T=inserer(tab[:n],element)+tab[n:]
    return T
    
        
            
   