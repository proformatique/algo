def maxi(M, c=0):
    n = len(M)
    idx = 1
    mx = abs(M[idx][c])
    for i in range(2, n):
        v = abs(M[i][c])
        if mx < v and v > 0:
            idx = i
            mx = v
    print(idx, v)
    return idx, v


def z(M,k):
    n = len(M)
    i, v = maxi(M)
    for c in range(n):
        M[i][c] =  M[k][c] - M[k][0]/v*M[i][c]

##
    
def printf(M):
    for e in M:
        print(e)
##            
            
def diagonale(M):
    n = len(M)
    p = 1
    for l in range(-n+1,
    for k in range(n):
        I = (i+k) % n
        J = (j+k) % n
        print(M[I][J])
##
            

def det2(M):
    d = M[0][0] * M[1][1] -  M[0][1] * M[1][0]
    print(' = ', d)
    return d

def C(M, i, j):
    C=[]
    n = len(M)
    for k in range(n):
        if k!= i:
            ln = []
            for l in range(n):
                if l != j:
                    ln.append(M[k][l])
            C.append(ln)
    return C
                    
                    
def det(M, i=-1, j=-1):
    A = C(M, i, j)
    n=len(A)
    if n == 2:
        return det2(A)
    else:
        c = 0
        k = 1
        for l in range(n):
            p = l+k+2
            c += (-1) ** p * A[l][k] * det(A, l, k)
        print('-'*20)
        return c
    

    '''
def det(M):
    if i == j == 0:
    else:
        for k in range(
        detij(M, i, j)
    '''
    '''
    x t y
    y x t
    t y x
    
    xxx + yyy + ttt
    - yxt - tyx - xty
    
    opérations élémentaires triangulariasation
    produit de la diagonale
    
    
    
    
    
    '''