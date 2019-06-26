def recherche(fichier,mot):
    l=[]
    i=0
    with open(fichier,'r')as fich:
        for line in fich:
            if mot in line:
                i+=1
                l=l+[i]
    return l
            
def inserer(tab,element):
    if len(tab)==1:
        if tab[0]<=element:
            tab =tab+[element]
        else:
            tab=[element]+tab
    else:
        j=len(tab)//2
        if element<=tab[j]:
            tab=inserer(tab[:j],element)+tab[j:]
        else:
            tab=tab[:j]+inserer(tab[j:],element)
    return tab
            
        