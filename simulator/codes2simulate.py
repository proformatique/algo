#:v"n>0,n,chiffre"
n = 5212
chiffre = ''
#:i
#:l
while n > 0:
    chiffre = n % 10  # Modulo : reste de la div. entière
    n //= 10          # n = n // 10 : // div entière
    print(chiffre)
    #:l

##:s
#:v"n>0,n,chiffre,u"
n = 5212
chiffre = ''
u = 0
#:i
#:l
while n > 0:
    chiffre = n % 10
    n //= 10
    u = u * 10 + chiffre
    print(chiffre)
    #:l

##:s
#:v"condition,nombre,cpt"
condition = False
nombre = 10908006000
cpt = 0
#:i
#:l
while True:   
    if nombre % 10 == 0:
        cpt = cpt + 1            
    #:l
    nombre = nombre // 10
    condition = nombre != 0
    if not condition:
        break
print("Nombre de zéro : ", cpt)

##:s
#:v"condition,nombre,somme"
condition = False
nombre = 123456789
somme = 0
#:i
#:l
while True:
    chiffre = nombre % 10
    somme += chiffre    ;#:l
    nombre //= 10       # chiffre supprimé
    condition = nombre != 0
    if not condition:
        break
print('Somme des chiffres ', somme)

##:s
#:v"condition,nombre,somme"
condition = False
nombre = 123456789
N = nombre
somme = 0
#:i
#:l
while True:
    chiffre = nombre % 10
    somme += chiffre ** 3  ; #:l
    nombre //= 10 
    condition = nombre != 0
    if not condition:
        break
estArmstrong = somme == N
print(N, ' est un nombre d\'Armstrong ', estArmstrong)

##:s
#:v"n>0,n,chiffre"
n = 19
chiffre = ''
#:i
#:l
while n > 0:
    chiffre = n % 2
    n //= 2
    print(chiffre)
    #:l
##:s
#:v"n>0,n,chiffre,codebin"
n = 19
chiffre = ''
codebin = ''
#:i
#:l
while n > 0:
    chiffre = n % 2
    n //= 2
    codebin = str(chiffre) + codebin
    print(chiffre)
    #:l
##:s
#:v"A,B,C"
A = B = C = True  # Affectation en série
#:i
A = not A                   ;#:l
B = not A                   ;#:l
C = (not A) and B           ;#:l
A = (A or B) and (not C)    ;#:l
B = (not B) or (not A)      ;#:l
##:s
#:v"A,B,C"
A = B = C = False
#:i
B = not B                   ;#:l
C = not B                   ;#:l
A = (not A) and B           ;#:l
B = (A or B) and (not C)    ;#:l
C = (not B) or (not A)      ;#:l
##:s
#:v"nA,nB,i,P"
# pour simuler la déclaration
P = nB = nA = i = ''
#:i
# pour simuler la lecture de A et B
A, B = -5, 2 # Affectation en parallèle
P = 0
nB = B
nA = A                  ;#:l
if nA < 0:
    nA = -nA            ;#:l
    nB = -nB            ;#:l
for i in range(1, nA+1):
    P = P + nB          ;#:l

##:s
#:v"A,B,i,R,i*B+R"
# pour simuler la déclaration
i = A = B = R = 0
#:i
#:l
A = 5 # remplace la lecture de A
B = 2 # remplace la lecture de B
if B > 0:
    i = 0           ;#:l
    R = A           ;#:l
    while R >= B:
        R = R - B         
        i = i + 1   ;#:l

##:s
#:v"tindice,taille,element"
# pour simuler la déclaration d'un tableau
tab = [5, 8, 7, 9, 5, 6, 3, 8]
taille = len(tab)
tindice = 0                 # preimer indice
element = tab[tindice]      # indexation
tlesindices = range(taille)
# Parcourir un tableau en utilisant for
for tindice in tlesindices:
    element = tab[tindice]
    print(tindice, element) ;#:l