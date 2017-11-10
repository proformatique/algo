# <demo> stop
# Parcourir un intervalle d'entiers

intervalle = range(10, 100, 20)
for element in intervalle:
    print(element)
# <demo> stop
# Parcourir une chaîne de caractères

texte = 'je suis un texte'
for caractere in texte:
    print(caractere)
# <demo> stop
# Parcourir une liste

liste = [12, 'sara', 15.5, 3+5j, True]
for element in liste:
    print(element)
# <demo> stop
# On importe le module turtle
import turtle as t

# Imbrication de boucles
for i in range(10):
    t.rt(36)
    for i in range(5):
        t.fd(54)
        t.rt(72)

# <demo> stop
# Tous les nombres pairs compris entre deux valeurs
## Construction
def pairs(a, b):
    v1 = (a + 1) // 2
    v2 = (b + 2) // 2
    for n in range(v1, v2):
        print(n * 2)
        
## Appel
v1 = eval(input('Entrer la première borne :'))
v2 = eval(input('Entrer la deuxième borne :'))
pairs(v1, v2)
# <demo> stop
# Tous les nombres pairs compris entre deux valeurs
# Sélection
def pairs2(a, b):
    for n in range(a, b+1):
        if n % 2 == 0:
            print(n)
# Appel
v1 = eval(input('Entrer la première borne :'))
v2 = eval(input('Entrer la deuxième borne :'))
pairs2(v1, v2)

    

    

