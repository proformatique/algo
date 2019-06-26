def recherche(nom_du_fichier,mot_à_chercher) -> list :
    A = []
    j = 0
    i = 0
    for l in nom_du_fichier :
        for elm in l :
            a = ''
            if elm != ' ' :
                a += elm 
            else :
                if a == mot_à_chercher :
                    j += 1
                    A[i] = j
                    i += 1
    return A 
    

    
def inserer(tab,element) -> list :
    if len(tab) == 0:
        tab[0] == element 
    elif len(tab) == 1:
        tab += [0]
        if tab[0] < element:
            tab[1] = element 
        else :
            tab[0],tab[1] = elm,tab[0]
    else:
        if element < tab[len(tab)//2]:
            T = inserer(tab[:(len(tab)//2)],element)
            return T + tab[len(tab)//2:]
        else :
            T = inserer(tab[(len(tab)//2):], element)
            return  tab[:(len(tab)//2)] + T
            

    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            