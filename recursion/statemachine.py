import random
def toint(s):
    som = 0
    for i in range(len(s)):
        som += int(s[~i]) * 2 ** i
    return som

def div(n, d):
    return n % d == 0
    
l3 = ["0000000000000000000",
'11'*3,
'11'*2,]

z = random.randint(0,1)
b0 = random.randint(1,2)
a = [random.randint(0,1) for i in range(6)]
l5 = ['0'*a[0],
'100'+'1'*a[0]+'011',
('101'*b0+'10'+(('0'+'1'*a[0]+'01')*a[1]+('0'+'1'*a[2]+'000')*a[3])*a[4]+'1')*a[5],
]

l32 = [
(('0'*a[0]+'1'+'1'*a[1]+'00')*a[2]+('1'+'1'*a[3]+'1'+'0'*a[4]+'1')*a[5]+'0')*a[5],
]

def dw(l, d):
    for s in l:
        n = toint(s)
        print(s, "=", n, "multiple de %d" % d, div(n, d))

dw(l32, 2)
dw(l32, 3)        


def etat0(mot, i=0):
    if i >= len(mot):
        print(mot, "Accepté")
    elif mot[i] == '0':
        etat0(mot, i+1)
    elif mot[i] == '1':
        etat1(mot, i+1)

def etat1(mot, i):
    if i >= len(mot) or mot[i] != '0' :
        print(mot, "Refusé")
    elif mot[i] == '0':
        etat2(mot, i+1)


def etat2(mot, i):
    if i >= len(mot):
        print(mot, "Refusé")
    elif mot[i] == '0':
        etat4(mot, i+1)
    elif mot[i] == '1':
        etat0(mot, i+1)

def etat3(mot, i):
    if i >= len(mot):
        print(mot, "Refusé")
    elif mot[i] == '0':
        etat1(mot, i+1)
    elif mot[i] == '1':
        etat2(mot, i+1)

def etat4(mot, i):
    if i >= len(mot):
        print(mot, "Refusé")
    elif mot[i] == '0':
        etat3(mot, i+1)
    elif mot[i] == '1':
        etat4(mot, i+1)

def evaluer(n):
    for i in range(n):
        mot = bin(i)[2:]
        etat0(mot)


def pile(n):
    return [i for i in range(n, 0, -1)]

N = 4
AP = pile(N)
BP = []
CP = []

piquets = {'A':AP, 'B':BP, 'C':CP}

def deplacer(frm, to):
    disc = piquets[frm].pop()
    piquets[to].append(disc)

def afficher(n):
    for i in range(n-1,-1,-1):
        na = piquets['A'][i:i+1]
        na = na[0] if len(na) else 0
        nb = piquets['B'][i:i+1]
        nb = nb[0] if len(nb) else 0
        nc = piquets['C'][i:i+1]
        nc = nc[0] if len(nc) else 0
        msg =  "{1:>{0}}|{1:<{0}} {2:>{0}}|{2:<{0}} {3:>{0}}|{3:<{0}}"
        print(msg.format(n ,na * "=",nb * "=",nc * "="))
    msg =  "{1:{0}}A{1:{0}} {1:{0}}B{1:{0}} {1:{0}}C{1:{0}}"
    print(msg.format(n,''),'\n')
    
def hanoi(A, B, C, n):
    if n > 0:
        hanoi(A, C, B, n-1)
        deplacer(A, C)
        print(n,':', A, '--->', C)
        afficher(N)
        hanoi(B, A, C, n-1)
    

options = ['Décompser', 'Résourdre', 'Combiner']

def quelobjectif():
    lo = []
    while True:
        print("Quel est l'objectif?")
        obj = input()
        if not obj:
            break
        print("Decrire l'objectif")
        desc = input()
        lo.append((obj, desc))
    assert len(lo) >= 1
    return lo

def quelresultat():
    lr = []
    while True:
        print("Quel est le résultat attendu?")
        res = input()
        if not res:
            break
        print("Decrire le résultat")
        desc = input()
        lr.append((res, desc))
    assert len(lr) >= 1
    return lr
    
def queldonnee():
    ld = []
    while True:
        print("Ajouter une donnée")
        dat = input()
        if not dat:
            break
        print("Decrire la donnée")
        desc = input()
        ld.append((dat, desc))
    assert len(ld) >= 1
    return ld

def comment():
    letapes = []
    print("Quelles sont les étapes de résolution?")
    while True:
        print("Ajouter une étape")
        etape = input()
        if not etape:
            break
        print("Decrire le résultat")
        desc = input()
        letapes.append((etapes, desc))
    assert len(letapes) >= 1
    return lr
    
questions = [quelobjectif, quelresultat, queldonnee, comment]
tasks = []
def analyser():
    for question in  questions:
        question()
    