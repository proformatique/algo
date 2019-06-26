# int() float() bool() ou eval()
x = eval(input('Entrez la valeur de x : '))
if x >= 0 :
    valeur_absolue = x
else:
    valeur_absolue = -x
print("La valeur absolue de", x, ' est ', valeur_absolue)

##
x = eval(input('Entrez la valeur de x : '))
valeur_absolue = x
if x < 0:
    valeur_absolue = -x

print("La valeur absolue de", x, ' est ', valeur_absolue)
###
def val_abs(x=n):
    if x >= 0 :
        valeur_absolue = x
    else:
        valeur_absolue = -x
    return valeur_absolue
    
n = eval(input('Entrez la valeur de n : '))
print("La valeur absolue de", n, ' est ', val_abs(n))


##


###

if c1 :
    bloc1
elif c2 :
    bloc2
elif c3 :
    bloc3
    .
    .
    .
else:
    autre