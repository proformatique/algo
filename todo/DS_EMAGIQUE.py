# Variables globales
#     0  1  2  3  4  5  6
T = [[0, 0, 0, 6, 0, 0, 0],  # 0
     [0, 4,13, 0,16, 1, 0],  # 1
     [0,12, 0, 0, 0,10, 0],  # 2
     [3, 0, 0, 0, 0, 0, 2],  # 3
     [0,11, 0, 0, 0, 9, 0],  # 4
     [0, 7, 5, 0, 8,14, 0],  # 5
     [0, 0, 0,15, 0, 0, 0]]  # 6


# les sommets (premier segment (0, 3) (3, 6))
sommets = [ [0 , 3], # 6
            [1 , 5], # 1
            [3 , 6], # 2
            [5 , 5], # 14
            [6 , 3], # 15
            [5 , 1], # 7
            [3 , 0], # 3
            [1 , 1]] # 4


def pas(pd, pf):
    
    if pf - pd == 0:
        pas = 0
    elif pf < pd:
        pas = -1
    else:
        pas = 1
    return pas


def sommeSegment(i_d, j_d, i_f, j_f):
    rows = abs(i_f - i_d)
    cols = abs(j_f - j_d)
    dist = rows if rows > cols else cols
    pas_i = pas(i_d, i_f)
    pas_j = pas(j_d, j_f)
    somme = 0
    # T est une variable globale : définie dans le programme principal
    for p in range(dist+1):
        somme += T[i_d + p * pas_i][j_d + p * pas_j]
    return somme


def etoileMagique() -> bool:
    i_d = sommets[0][0] # sommets est une variable globale
    j_d = sommets[0][1]
    i_f = sommets[2][0]
    j_f = sommets[2][1]
    sm = sommeSegment(i_d, j_d, i_f, j_f)
    condition = True
    for i in range(1, len(sommets)):
        i_d = sommets[i][0]
        j_d = sommets[i][1]
        i_f = sommets[(i + 2) % 8][0]
        j_f = sommets[(i + 2) % 8][1] # % 8 pour les deux derniers segments
        condition = sm == sommeSegment(i_d, j_d, i_f, j_f)
        if not condition:
            return False
    return True

# DS 
def remplissage2(tab):
    a = 1
    i, j = 0, 0
    while a <= 100: # for a in range(1, 101):
        T[i][j] = a
        a += 1
        if j < i:
            j += 1
        elif i > 0:
            i -= 1
        elif i == 0:
            i = j +  1
            j = 0

T = [[0] * 10 for i in range(10)]
remplissage2(T)
print(T)
