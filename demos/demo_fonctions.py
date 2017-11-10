# <demo> stop
# Définition de procédure

def maProcedure(param):
    resultat = param * 6
    print(resultat)
# <demo> stop
# Appel de procédure

maProcedure(654)
maProcedure(5)
maProcedure(4)

# <demo> stop
# Définition de fonction

def maFonction(param):
    resultat = param * 2
    return resultat

# <demo> stop
# Appel de fonction

argument = 5
x = maFonction(argument)
print(x)