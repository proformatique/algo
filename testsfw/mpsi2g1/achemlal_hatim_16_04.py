def recherche(fichier,mot):
    with open(fichier,encoding='utf-8') as doc:
        contenu=doc.readlines()
    b=[]
    for i in range (len(contenu)):
        if mot in contenu[i].split():
            b+=[i+1]
    return b
    
    

def inserer(tab,element)->list:
    if len(tab)==0:
        return [element]
    elif tab[len(tab)//2]<element:
        return tab[:len(tab)//2 +1]+inserer(tab[len(tab)//2  +1:],element)
    else:
        return inserer(tab[:len(tab)//2],element)+tab[len(tab)//2:]
    
    
    
    
    
    
    
    
    
    
    
    