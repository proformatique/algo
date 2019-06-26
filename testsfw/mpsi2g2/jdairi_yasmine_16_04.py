def inserer(tab,element):
    c = tab
    if element > c[len(c)//2]:
        if len(c)>1:
            c = c[len(c)//2+1:]
            res = inserer(c,element)
        else:
            res = tab.index(c[len(c)//2])+1
    elif element < c[len(c)//2]:
        if len(c)>1:
            c = c[:len(c)//2]
            res = inserer(c,element)
        else:
            res = tab.index(c[len(c)//2])-1
    elif element == c[len(c)//2]:
        res = tab.index(c[len(c)//2])+1
    q = []
    for i in range(len(tab)+1):
        q+=[0]
    for i in range(res,len(tab)):
        q[i+1] = tab[i]
    for i in range(res):
        q[i] = tab[i]
    q[res] = element
    return q
def recherche(nomdufichier,mot):
    l = []
    i = 1
    with open(nomdufichier,encoding='utf-8') as f:
        for line in f:
            if mot in f:
                l += [i]
                i += 1
            else:
                i+=1
    return l
                
                
        
    