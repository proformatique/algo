def rle(texte:str)->str:
    texte1=str()
    s=''
    if texte==texte[0]*len(texte):
        return str(len(texte))+texte[0]
    else:
        for i in range(len(texte)-1):
            texte2=str()
            if texte[0:i+1]==texte[0]*(i+1) and bool(texte[0]==texte[i+1])==False:
                texte1=texte1+rle(texte[0:i+1])
                texte2=texte[i+1:len(texte)]
                s=texte1+rle(texte2)
        return s
                
                   