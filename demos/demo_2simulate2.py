
# <demo> stop
 # Script 

condition = False
nombre = 123456789
N = nombre
somme = 0
# Initialisation faite
# BPoint
while True:
    chiffre = nombre % 10
    somme += chiffre ** 3  ; # BPoint
    nombre //= 10 
    condition = nombre != 0
    if not condition:
        break
estArmstrong = somme == N
print(N, ' est un nombre d\'Armstrong ', estArmstrong)


# <demo> stop
 # Script 


n = 19
chiffre = ''
# Initialisation faite
# BPoint
while n > 0:
    chiffre = n % 2
    n //= 2
    print(chiffre)
    # BPoint

# <demo> stop
 # Script 


n = 19
chiffre = ''
codebin = ''
# Initialisation faite
# BPoint
while n > 0:
    chiffre = n % 2
    n //= 2
    codebin = str(chiffre) + codebin
    print(chiffre)
    # BPoint

# <demo> stop
 # Script 


A = B = C = True  # Affectation en sÃ©rie
# Initialisation faite
A = not A                   ;# BPoint
B = not A                   ;# BPoint
C = (not A) and B           ;# BPoint
A = (A or B) and (not C)    ;# BPoint
B = (not B) or (not A)      ;# BPoint

# <demo> stop
 # Script 


A = B = C = False
# Initialisation faite
B = not B                   ;# BPoint
C = not B                   ;# BPoint
A = (not A) and B           ;# BPoint
B = (A or B) and (not C)    ;# BPoint
C = (not B) or (not A)      ;# BPoint

# <demo> stop
 # Script 


# pour simuler la dÃ©claration
P = nB = nA = i = ''
# Initialisation faite
# pour simuler la lecture de A et B
A, B = -5, 2 # Affectation en parallÃ¨le
P = 0
nB = B
nA = A                  ;# BPoint
if nA < 0:
    nA = -nA            ;# BPoint
    nB = -nB            ;# BPoint
for i in range(1, nA+1):
    P = P + nB          ;# BPoint


# <demo> stop
 # Script 


# pour simuler la dÃ©claration
i = A = B = R = 0
# Initialisation faite
# BPoint
A = 5 # remplace la lecture de A
B = 2 # remplace la lecture de B
if B > 0:
    i = 0           ;# BPoint
    R = A           ;# BPoint
    while R >= B:
        R = R - B         
        i = i + 1   ;# BPoint


# <demo> stop
 # Script 


# pour simuler la dÃ©claration d'un tableau
tab = [5, 8, 7, 9, 5, 6, 3, 8]
taille = len(tab)
tindice = 0                 # preimer indice
element = tab[tindice]      # indexation
tlesindices = range(taille)
# Parcourir un tableau en utilisant for
for tindice in tlesindices:
    element = tab[tindice]
    print(tindice, element) ;# BPoint