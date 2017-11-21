
def creation(L, C):
    # 
    R2D = []
    for i in range(L):
        ligne = []
        # ligne = [None] * C
        for j in range(C):
            ligne += [None] # ligne.append(None)
        R2D += [ligne]
    return R2D

def moyenne2D(notes):
    L = len(notes)
    C = len(notes[0]) - 1
    for i in range(L):
        somme = 0
        for j in range(C):
            somme += notes[i][j]
        moy = somme / C
        notes[i][C]
# Q 1: Non, type, valeurs calculées...
# Q 2 
N = eval(input('Entrer le nombre d\'élèves '))
notes = creation(N, 4)
        
    