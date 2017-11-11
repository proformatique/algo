#v:"n>0,n,chiffre"
n = 5212
chiffre = ''
#i:
#bp:
while n > 0:
    chiffre = n % 10  # Modulo : reste de la div. entière
    n //= 10          # n = n // 10 : // div entière
    print(chiffre)
    #bp:

##s:
#v:"n>0,n,chiffre,u"
n = 5212
chiffre = ''
u = 0
#i:
#bp:
while n > 0:
    chiffre = n % 10
    n //= 10
    u = u * 10 + chiffre
    print(chiffre)
    #bp:

##s:
#v:"condition,nombre,cpt"
condition = False
nombre = 10908006000
cpt = 0
#i:
#bp:
while True:   
    if nombre % 10 == 0:
        cpt = cpt + 1            
    #bp:
    nombre = nombre // 10
    condition = nombre != 0
    if not condition:
        break
print("Nombre de zéro : ", cpt)

##s:
#v:"condition,nombre,somme"
condition = False
nombre = 123456789
somme = 0
#i:
#bp:
while True:
    chiffre = nombre % 10
    somme += chiffre    ;#bp:
    nombre //= 10       # chiffre supprimé
    condition = nombre != 0
    if not condition:
        break
print('Somme des chiffres ', somme)
