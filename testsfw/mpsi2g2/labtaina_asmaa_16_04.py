def recherche(nom_du_fichier,mot_a_chercher):
    L1 = []
    L2 = []
    n = 0
    with open(nom_du_fichier,'r',encoding='utf-8') as fc:
        for line in fc:
            if mot_a_chercher in line:
                L1 +=[1]
            else:
                L1 +=[0]
        n = len(L1)
        assert n>0
        for i in range(n-1):
            if L1[i]=='1':
                L2+=[i+1]
        if L1[n-1]=='1':
            L2 += [n-1]
        return L2

def inserer(tab,element):
    n =len(tab)
    L=[]
    c=0
    a=0
    b=0
    if n==1:
        if element>tab[0]:
            L+=[tab[0]]+[element]
        else:
            L+=[element]+[tab[0]]
        return L
    else:
        for i in range(n):
            c==n//2
            if element==tab[c]:
                return [tab[:c+1]+[element]+tab[c+1:]]
            elif element>tab[c]:
                a = c+1
                b = n
                return inserer(tab[a:b],element)
            else:
                a=0
                b = c-1
                return inserer(tab[a:b],element)
                
                
                
                
                
                
    
               
    
    
    
    
    
    
    