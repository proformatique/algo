#v:"condition,nombre,somme"
condition = False
nombre = 123456789
N = nombre
somme = 0
#i:
#bp:
while True:
    chiffre = nombre % 10
    somme += chiffre ** 3  ; #bp:
    nombre //= 10 
    condition = nombre != 0
    if not condition:
        break
estArmstrong = somme == N
print(N, ' est un nombre d\'Armstrong ', estArmstrong)

##s:
#v:"n>0,n,chiffre"
n = 19
chiffre = ''
#i:
#bp:
while n > 0:
    chiffre = n % 2
    n //= 2
    print(chiffre)
    #bp:
##s:
#v:"n>0,n,chiffre,codebin"
n = 19
chiffre = ''
codebin = ''
#i:
#bp:
while n > 0:
    chiffre = n % 2
    n //= 2
    codebin = str(chiffre) + codebin
    print(chiffre)
    #bp:
##s:
#v:"A,B,C"
A = B = C = True  # Affectation en série
#i:
A = not A                   ;#bp:
B = not A                   ;#bp:
C = (not A) and B           ;#bp:
A = (A or B) and (not C)    ;#bp:
B = (not B) or (not A)      ;#bp:
##s:
#v:"A,B,C"
A = B = C = False
#i:
B = not B                   ;#bp:
C = not B                   ;#bp:
A = (not A) and B           ;#bp:
B = (A or B) and (not C)    ;#bp:
C = (not B) or (not A)      ;#bp:
##s:
#v:"nA,nB,i,P"
# pour simuler la déclaration
P = nB = nA = i = ''
#i:
# pour simuler la lecture de A et B
A, B = -5, 2 # Affectation en parallèle
P = 0
nB = B
nA = A                  ;#bp:
if nA < 0:
    nA = -nA            ;#bp:
    nB = -nB            ;#bp:
for i in range(1, nA+1):
    P = P + nB          ;#bp:

##s:
#v:"A,B,i,R,i*B+R"
# pour simuler la déclaration
i = A = B = R = 0
#i:
#bp:
A = 5 # remplace la lecture de A
B = 2 # remplace la lecture de B
if B > 0:
    i = 0           ;#bp:
    R = A           ;#bp:
    while R >= B:
        R = R - B         
        i = i + 1   ;#bp:

##s:
#v:"tindice,taille,element"
# pour simuler la déclaration d'un tableau
tab = [5, 8, 7, 9, 5, 6, 3, 8]
taille = len(tab)
tindice = 0                 # preimer indice
element = tab[tindice]      # indexation
tlesindices = range(taille)
# Parcourir un tableau en utilisant for
for tindice in tlesindices:
    element = tab[tindice]
    print(tindice, element) ;#bp: