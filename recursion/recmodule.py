import os




def tree(path, sep=''):
    ls = os.listdir(path)
    for file in ls:
        p = sep
        print(p, file, sep='')
        if os.path.isdir(path+'\\'+file):  
            tree(path+'\\'+file, '    '+ sep)

path = os.path.abspath('.')
tree(path)

def triparfusion(t):
    #print(t)
    if len(t) <= 1:
        return t
    m = len(t) // 2
    A = t[:m]
    B = t[m:]
    A = triparfusion(A)
    B = triparfusion(B)
    C = fusion(A[:], B[:])
    return C
    

def fusion(t1, t2):
    #print(t1, t2)
    i, j = 0, 0
    t = []
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            t.append(t1[i])
            i += 1
        else:
            t.append(t2[j])
            j += 1
    while i < len(t1):
        t.append(t1[i])
        i += 1

    while j < len(t2):
        t.append(t2[j])
        j += 1
    return t
