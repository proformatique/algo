# Parcours d'une liste
liste = [1, 'a', 2.5]

for element in liste:
    print(element)

# Parcours d'une tuple  
nuplet = 1, 'a', 2.5 
for element in nuplet:
    print(element)

# Parcours d'une chaîne 
texte = 'cpge tsi' 
for car in texte:
    print(car)

# Parcours des valeurs de range
intervalle = range(1, 20, 5) # start = 0, step = 1
for valeur in intervalle:
    print(valeur)

# Parcours des valeurs de zip
collection = zip(liste, nuplet, texte)
for var in collection:
    print(var)

# Parcours des valeurs de enuemerate
for num, val in enumerate(texte):
    print(num, val)






