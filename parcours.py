def saisie(tab):
    taille = len(tab) # variable locale
    print('Vous allez saisir', taille, 'valeurs')
    for i in range(taille):
        tab[i] = eval(input('\n\t tab['+str(i)+'] = ? '))

# Appel
taille = 5  # variable globale
A = [0] * taille
saisie(A)

##
def affichage(tab):
    taille = len(tab)
    print('Affichage de ', taille, 'valeurs ')
    for i in range(taille):
        print('tab[', i, '] = ', tab[i], sep='', end='; ')

# Appel
A = [1, 2, 3, 4, 5, 8]
affichage(A)
