######## <demo_boucles.py> #########
''' Les structures itératives permettent de répéter l'éxécution du code
while condition:
    bloc de code
    instr2
    instr3
    
tantque codition faire
    bloc de code
fintq
'''
# <demo> stop
x = 0         
while x <= 10: 
    print(x)
    x = x + 1
# <demo> stop
'''
seq = {0,1,2,3}
seq = range(start=0, stop, step=1) : intervalle [start, stop[
for var in seq:
    bloc de code

pour var ← start jusqua stop pas ← step faire
    bloc de code
finpour
'''
# <demo> stop
for x in range(10):
    print(x)
# <demo> stop
'''
repeter
    bloc de code
tanque condition

while True:
    bloc de code
    if condition:
        break   # sortir

'''  
# <demo> stop     
while True: 
    choix = input('Entrer q pour quitter ')
    if not (choix != 'q'):
        print('Bye !')
        break
# <demo> silent
# the mark below makes this block as silent
# stop silent auto

######## Fin de la démonstration <demo_boucles.py> ##############