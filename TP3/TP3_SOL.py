# Transcription de l'algorithme

##
def affichediagonale(T2D):
    L = len(T2D)
    for i in range(L):
        print('T [', i, '][', i, '] = ', T2D[i][i])


def permuterColonnes(T2D, i, j):
    for k in range(len(T2D)):
        T2D[k][i], T2D[k][j] = T2D[k][j], T2D[k][i]

##
def permuterLignes(T2D, i, j):
    for k in range(len(T2D[0])):
        T2D[i][k], T2D[j][k] = T2D[j][k], T2D[i][k]


def creation(L, C):
    R2D = []
    for i in range(L):
        ligne = []
        # on peut aussi utiliser ligne = [None] * C
        for j in range(C):
            ligne += [None] # ligne.append(None)
        R2D += [ligne]
    return R2D
    
def saisieNotes():
    for i in range(len(notes)):
        noms[i] = input('Entrer le nom de l\'élève :')
        for j in range(len(notes[0]-1)):
            notes[i][j] = eval(input('Entrer la note '+str(i+1)+' : '))
            

def moyenne2D(notes):
    L = len(notes)
    C = len(notes[0]) - 1
    for i in range(L):
        somme = 0
        for j in range(C):
            somme += notes[i][j]
        moy = somme / C
        notes[i][C] = moy

def moyenneEleve(nom):
    ielv = -1
    for i in range(N):
        if noms[i] == nom:
            ielv = i # indice de l'élève
            print(noms[ielv], end='')
            for j in range(C):
                print(notes[ielv][j])
    if ielv == -1:
        prnt('Pas d\'élève avec le nom ' + nom)

def moyenne2D(notes):
    L = len(notes)
    C = len(notes[0]) - 1
    ttl = sum(coefficient) # somme()
    for i in range(L):
        somme = 0
        for j in range(C):
            somme += notes[i][j] * coefficient[j]
        moy = somme / ttl
        notes[i][C] = moy

# Mini projet
# Q 1: Non, Types différents (str, float), Valeurs calculées (moyenne), Mélange des données (Noms, DSs) et résultats (Moyenne), ...
# Q 2
if __name__ == '__main__':
    L = 5 # L = len(T)
    C = 5 # C = len(T[0])
    T = [[0] * C for i in range(L)]
    
    for i in range(L):
        for j in range(C):
            print('Entrer la valeur de T [', i, '][', j, ']')
            T[i][j] = input()
    ##
    for i in range(L):
        for j in range(C):
            print('La valeur de T [', i, '][', j, '] est ', T[i][j])

    N = eval(input('Entrer le nombre d\'élèves '))
    C = 4
    notes = creation(N, 4)
    noms = [''] * N
        
    