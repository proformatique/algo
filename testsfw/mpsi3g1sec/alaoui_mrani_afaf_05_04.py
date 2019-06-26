def rle(texte)-> str:
    T = len(texte)
    a = texte[0]
    j = 1
    c =''
    for i in range(1,T):
        if texte[i] == a :
            j += 1
        else :
            c += str(j)+texte[i-1]
            a = texte[i]
            j = 1
    return c+str(j)+texte[-1]

def decompression_rle(texte) -> str:
    chiffres ='0123456789'
    k = 0
    a =''
    b =''
    c =''
    for i in range(len(texte)):
        if texte[i] not in chiffres :
            a = texte[i]
            for h in range(k,i):
                b += texte[h]
                k = i+1
                c += int(b)*a
    return c