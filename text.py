liste = [45,  'j', 1j]
for var in liste:
    print(var)

texte = '''mpsi2g2'''
for car in texte:
    print(car)

nuplet = 0, 'a', 3.5
for element in nuplet:
    print(element)

intervalle = range(5, 500, 100) # start = 0, stop = 1
for x in intervalle:
    print(x)
##
collection = zip(intervalle, texte, nuplet)
for element in collection:
    print(element)
##
for num, valeur in enumerate(texte, 1):
    print(num, valeur)




