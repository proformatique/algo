def rle(T):
    l=len(T)
    T2=''
    cpt=1
    if l==0:
        return '0'
    elif l==1:
        return T
    else:        
        for k in range(l-1):
            ch,ch2=T[k],T[k+1]
            if ch==ch2:
                cpt+=1
            else:
                if cpt==1:
                    T2+=ch
                else:
                    c=str(cpt)+ch
                    T2+=c
                cpt=1    
        return T2
##
    
                        