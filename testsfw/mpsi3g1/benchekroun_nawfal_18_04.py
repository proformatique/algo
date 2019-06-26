def recherche(nom_du_fichier,mot_a_rechercher):
    """
    >>>recherche(text.txt, 'que')
    []
    """
    with open(nom_du_fichier,"w",encoding="utf8") as data:
        L=[]
        j=0
        for line in data:
            j+=1
            if mot_a_rechercher in data:
                L+=[j]
    return L
def inserer(tab,element):
    """
    >>> inserer([],0)
    [0]
    >>> inserer([1],2)
    [1 , 2]
    >>> inserer([1],0)
    [0 , 1]
    >>> inserer([0,1,2,3,4,5,6,7,8,9],3)
    [0 , 1 , 2 , 3 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,]
    """
    if len(tab)==0:
        tab+=[element]
        return tab
    elif len(tab)==1:
        if tab[0]>=element:
            return [element]+tab
        else:
            return tab+[element]
    l=len(tab)//2
    if tab[l]<=element:
        inserer(tab[l+1:len(tab):1],element)
    elif tab[l]>=element:
        inserer(tab[0:l+1:1],element)
    else:
        return tab[0:l+1:1]+[element]+tab[l+1:len(tab):1]
        
inserer([],0)
def inserer([1],0)
def inserer([1],2)
def inserer([0,1,2,3,4,5,7,8,9],8)            
            
if __name__=="__main":
    import doctest as dt
    dt.testmod()
