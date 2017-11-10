#Question 1.
def sommeRangee(cm, r) -> int:
    '''Retourne la somme de la rangée r du carré magique cm.
    Donnée
    ------
        cm : list, carré magique
        r : int, indice de la rangée
    Sortie
    ------
        sommeRg : int, somme de la rangée
    '''
    sommeRg = 0
    for i in range(len(cm)):
        sommeRg += cm[r][i]
    return sommeRg
    
    
#Question 2.    
def sommeColonne(cm, c) -> int:
    '''Retourne la somme de la colonne c du carré magique cm.
    Donnée
    ------
        cm : list, carré magique
        c : int, indice de la colonne
    Sortie
    ------
        sommeCl : int, somme de la colone
    '''
    sommeCl = 0
    for i in range(len(cm)):
        sommeCl += cm[i][c]
    return sommeCl

#Question 3.
def sommeDiagPrincipale(cm, d) -> int:
    '''Retourne la somme de la diagonale principale.
    Donnée
    ------
        cm : list, carré magique
        d : int, 1 pour la première diagonale et 2 pour la deuxième diagonale
    Sortie
    ------
        sommeDg : int, somme de la diagonale
    '''
    sommeDg = 0
    for i in range(len(cm)):
        idiag = i if d == 1 else len(cm) - 1 - i
        sommeDg += cm[i][i]
    return sommeDg

#Question 4.a
def magique(cm) -> bool:
    '''Retourne True si cm est magique.
    Donnée
    ------
        cm : list, carré d'ordre N.
    Sortie
    ------
        magique : bool, True si cm est magique, sinon False.
    '''
    magique = True
    constanteMagique = sommeColonne(cm, 0)
    magique &= constanteMagique == sommeDiagPrincipale(cm, 1)
    magique &= constanteMagique == sommeDiagPrincipale(cm, 2)
    for i in range(len(cm)):
        magique &= constanteMagique == sommeColonne(cm, i)
        magique &= constanteMagique == sommeRangee(cm, i)
        if not magique:
            break
    return magique
    
#Question 4.b        
def magiqueNormal(cm) -> bool:
    '''Retourne True si cm est normal.
    Donnée
    ------
        cm : list, carré magique
    Sortie
    ------
        normal : bool, True si cm est normal, sinon False.
    '''
    
    if not magique(cm):
        normal = False
    else:
        normal = True
        N = len(cm)
        serie = [0] * N ** 2
        for i in range(N):
            for j in range(N):
                if 1 <= cm[i][j] <= N ** 2:
                    serie[cm[i][j]-1] = cm[i][j]
                else:
                    normal = False
                    break
    for i in range(N**2):
        normal &= serie[i] != 0
        if not normal:
            break
    return normal
        
#Question 5.   
def sommeMagic(cm1, cm2, signe) -> list:
    '''Retourne un carrée magique somme de cm1 et cm2.
    Données
    ------
        cm1 : list, carré magique.
        cm2 : list, carré magique.
        signe : str, signe '+' pour la somme '-' pour la soustraction
    Sortie
    ------
        sommeMg : list, somme ou soustraction terme à terme de cm1 et cm2.
    '''
    N = len(cm1)
    M = len(cm2)
    sommeMg = []
    assert N == M and signe in '+-'
    s = 1 if signe == '+' else -1
    for i in range(N):
        ligne = []
        for j in range(N):
            ligne += [cm1[i][j] + s * cm2[i][j]]
        sommeMg += [ligne]
    return sommeMg

#Question 6.
def reduireCMagique(cm) -> list:
    '''Retourne une copie de cm après réduction.
    Données
    ------
        cm : list, carré magique d'ordre M.
    Sortie
    ------
        cm_1 : list, copie réduite de cm.
    '''
    N = len(cm)
    cm_1 = []
    for i in range(N):
        ligne = []
        for j in range(N):
            ligne += [cm[i][j] - 1]
        cm_1 += [ligne]
    return cm_1
    
    
#Question 7.
def divisionMagique(i, j, M) -> tuple:
    '''Retourne un tuple r, c.
    Données
    -------
        M : int ordre du premier carré magique
        i : int, indice de ligne d'une case dans le carrée d'ordre N * M.
        j : int, indice de colonne d'une case dans le carrée d'ordre N * M.
    Sortie
    ------
        r : int, premier indice du sous-carré d'ordre N dans le carré final.
        c : int, deuxième indice du sous-carré d'ordre N dans le carré final.
    '''
    r = i // M
    c = j // M
    return r, c
    
#Question 8.
def produitMagique(cm1, cm2) -> list:
    '''Retourne le produit de cm1 et cm2.
    Données
    ------
        cm1 : list, carré magique d'ordre M.
        cm2 : list, carré magique d'ordre N.
    Sortie
    ------
        produitMg : list, produit de cm1 et cm2.
    '''
    M = len(cm1)
    N = len(cm2)
    MxN = M * N
    cmr = reduireCMagique(cm2)
    produitMg = []
    for i in range(MxN):
        ligne = []
        for j in range(MxN):
            r, c = divisionMagique(i, j, M)
            ligne += [M ** 2  * cmr[r][c]]
        produitMg += [ligne]
    return produitMg
                    
#Question 9.
def additionMagique(cmf, cmm) -> list:
    '''Retourne une copie du damier final après adition de cmm à tous les sous-damiers.
    Données
    ------
        cmf : list, carré magique final d'ordre M x N.
        cmm : list, carré magique d'ordre M.
    Sortie
    ------
        cmfNormal : list, produit final normal.
    '''
    MxN = len(cmf)
    M = len(cmm)
    #produitMg = [[0] * M * N for n in range(M * N) ]
    cmfNormal = []
    for i in range(MxN):
        ligne = []
        for j in range(MxN):
            r, c = i % M, j % M
            ligne += [cmf[i][j]  + cmm[r][c]]
        cmfNormal += [ligne]
    return cmfNormal
    

M = [[4, 9, 2],
[3, 5, 7],
[8, 1, 6]
]

N = [
[4, 14, 15, 1],
[9, 7, 6, 12],
[5, 11, 10, 8],
[16, 2, 3, 13]
]


MF = produitMagique(M, N)
MFN = additionMagique(MF, M)

"""
In [25]: MF
Out[25]: 
[[27, 27, 27, 117, 117, 117, 126, 126, 126, 0, 0, 0],
 [27, 27, 27, 117, 117, 117, 126, 126, 126, 0, 0, 0],
 [27, 27, 27, 117, 117, 117, 126, 126, 126, 0, 0, 0],
 [72, 72, 72, 54, 54, 54, 45, 45, 45, 99, 99, 99],
 [72, 72, 72, 54, 54, 54, 45, 45, 45, 99, 99, 99],
 [72, 72, 72, 54, 54, 54, 45, 45, 45, 99, 99, 99],
 [36, 36, 36, 90, 90, 90, 81, 81, 81, 63, 63, 63],
 [36, 36, 36, 90, 90, 90, 81, 81, 81, 63, 63, 63],
 [36, 36, 36, 90, 90, 90, 81, 81, 81, 63, 63, 63],
 [135, 135, 135, 9, 9, 9, 18, 18, 18, 108, 108, 108],
 [135, 135, 135, 9, 9, 9, 18, 18, 18, 108, 108, 108],
 [135, 135, 135, 9, 9, 9, 18, 18, 18, 108, 108, 108]]

In [26]: MFN
Out[26]: 
[[31, 36, 29, 121, 126, 119, 130, 135, 128, 4, 9, 2],
 [30, 32, 34, 120, 122, 124, 129, 131, 133, 3, 5, 7],
 [35, 28, 33, 125, 118, 123, 134, 127, 132, 8, 1, 6],
 [76, 81, 74, 58, 63, 56, 49, 54, 47, 103, 108, 101],
 [75, 77, 79, 57, 59, 61, 48, 50, 52, 102, 104, 106],
 [80, 73, 78, 62, 55, 60, 53, 46, 51, 107, 100, 105],
 [40, 45, 38, 94, 99, 92, 85, 90, 83, 67, 72, 65],
 [39, 41, 43, 93, 95, 97, 84, 86, 88, 66, 68, 70],
 [44, 37, 42, 98, 91, 96, 89, 82, 87, 71, 64, 69],
 [139, 144, 137, 13, 18, 11, 22, 27, 20, 112, 117, 110],
 [138, 140, 142, 12, 14, 16, 21, 23, 25, 111, 113, 115],
 [143, 136, 141, 17, 10, 15, 26, 19, 24, 116, 109, 114]]
"""
