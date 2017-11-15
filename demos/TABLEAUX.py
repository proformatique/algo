
# PARCOURIR LES INDICES
taille = 5
lesindices = range(taille)
for indice in lesindices:
    print(indice)

# CONSTRUIURE LE TABLEAU 1D
'''
Algorithme tab
constantes
    taille ← 5
variables
    Tab1D[taille]  : type
'''
taille = 5
lesindices = range(taille)
# INITIALISATION
Tab1D = []  # On utilise une liste pour représenter le tableau
for indice in lesindices:
    print(indice)
    valeur = None # pas de valeur (tableau vide)
    # CONSTRUCTION
    Tab1D += [valeur] # concaténation des listes
    print(Tab1D)
# RENVOI DU RESULTAT
print(Tab1D)

# Autre méthode : répétition
taille = 5
Tab1Dr = [None] * taille
print(Tab1Dr)

# Autre méthode : liste en compréhension
taille = 5
Tab1Dc = [None for i in range(taille)] 
print(Tab1Dc)

# Tableaux à deux dims.
# PARCOURIR LES INDICES
##
taille1 = 4
taille2 = 3
lesILignes = range(taille1)
lesIColonnes = range(taille2)
for indiceL in lesILignes:
    for indiceC in lesIColonnes:
        print(indiceL, indiceC)
##

# CONSTRUIURE LE TABLEAU 2D
'''
Algorithme tab2d
constantes
    taille1 ← 4
    taille1 ← 3
variables
    Tab2D[taille1][taille2] : type
'''
##
taille1 = 4
taille2 = 3
lesILignes = range(taille1)
lesIColonnes = range(taille2)
Tab2D = []
for indiceL in lesILignes:
    ligne = []
    for indiceC in lesIColonnes:
        valeur = None
        ligne += [valeur]
        print(indiceL, indiceC,ligne)
    Tab2D += [ligne]
    print(Tab2D)
print(Tab2D)
##

