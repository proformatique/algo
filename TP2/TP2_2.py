'''Algorithmes de base : Manipulation des tableaux 1D & 2D.
A. MHAMEDI
LYDEX 2017/18
Objectifs:
    1 - Opérations sur les tableaux à 2D?
        - Produit terme à terme
        - Somme terme à terme
    3 - Calcul matriciel
        - Trace
        - diagonale
        - produit
'''
def saisie2D(D2):
    Nl = len(D2)
    Nc = len(D2[0])
    print('Saisie de tableau de dim. (',Nl, 'x', Nc,')')
    for i in range(Nl):
        for j in range(Nc):
            D2[i][j] = eval(input(str(i)+', '+str(j)+'? '))
        
def affichage2D(D2):
    Nl = len(D2)
    Nc = len(D2[0])
    print('Affichage de tableau de dim. (',Nl, 'x', Nc,')')
    for i in range(Nl):
        for j in range(Nc):
            print('(',i,',',j,') = ',D2[i][j])
        
    
def diagonale(D2) -> list:
    Nl = len(D2)
    Nc = len(D2[0])
    assert Nl == Nc
    diag = [None] * Nl
    # D = []
    for i in range(Nl):
        diag[i] = D2[i][i]
        # D += [D2[i][i]] # ou D.append(D2[i][j])
    return diag

def trace(D2) -> list:
    Nl = len(D2)
    Nc = len(D2[0])
    assert Nl == Nc
    trc = 0
    for i in range(Nl):
        trc += D2[i][i]
    return trc

def sommeAB(A, B):
    nla = len(A)
    nca = len(A[0])
    nlb = len(B)
    ncb = len(B[0])
    assert nla == nlb and nca == ncb
    Sab = []
    for i in range(nla):
        ligne = []
        for j in range(nca):
            ligne += [A[i][j] + B[i][j]]
        Sab += [ligne]
    return Sab

def produitAB(A, B):
    nla = len(A)
    nca = len(A[0])
    nlb = len(B)
    ncb = len(B[0])
    assert nla == nlb and nca == ncb
    Pab = []
    for i in range(nla):
        ligne = []
        for j in range(nca):
            ligne += [A[i][j] * B[i][j]]
        Pab += [ligne]
    return Pab
##
def produitM(A, B):
    nla = len(A)
    nca = len(A[0])
    nlb = len(B)
    ncb = len(B[0])
    assert nca == nlb
    Pab = []
    for i in range(nla):
        ligne = []
        for j in range(ncb):
            s = 0
            for k in range(nca):
                s += A[i][k] * B[k][j]
            ligne += [s]
        Pab += [ligne]
    return Pab

# Programme Principal
#A = creation(N,M)
A = [[0,0],[0,0]]
saisie2D(A)
affichage2D(A)
print(diagonale(A))
I = [[1,0,0],[0,1,0],[0,0,1]]
print(produitM(I, I))