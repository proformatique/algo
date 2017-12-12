# <demo> stop
# STR - opérations de base
t = 'texte'
# indexation
# positive
print(t[0])
# négative
print(t[-1])
# slicing
print(t[::-1])
# str immuable
print(t[0] = '7')

# <demo> stop
texte = 'un texte'
texte[0]         # indexation
texte[0] = 'M'   # /!\ affectation 
'text' + 'e'     # concaténation
'text' 'e'       # concaténation auto.
'text' 'e' * 6   # c. auto. et répétition 
'text' + 'e' * 6 # c.  et répétition
'texte'[::]      # slicing
'texte'[::-1]    # slicing pas négatif
'texte'[::2]     # slicing pas positif

# <demo> stop
# STR - Formatage - %
"%s : %s" % (1, 2)
"%s : %s" % ('a', 'c')
"%s : %d" % ('a', 'c')
"%s : %d" % ('a', 5)

# <demo> stop
# STR - Formatage - str.format()
"{} : {}".format('a', 5)
"Nom : {}\nPrénom{}".format('alaoui', 'ali')
print("Nom : {}\nPrénom{}".format('alaoui', 'ali'))
print("Nom : {1:20}\nPrénom{0:20}".format('alaoui', 'ali'))
print("Nom : {1:>20}\nPrénom : {0:>20}".format('alaoui', 'ali'))