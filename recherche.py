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



def appartient(x, tab) -> bool:
    '''Teste si x fait partie de tab.
    Donnée
    ------
        tab : list, tableau d'entiers
        x   : int, valeur à chercher
    Sorite
    ------
        trouve : bool, True si x existe dans tab,
         False sinon
    Exemples
    >>> appartient(0, [])
    False
    >>> appartient(0, [0, 5, 8])
    True
    '''
    trouve = False
    for elm in tab:
        if elm == x:
            trouve = True
            break
    return trouve
    
    
##
def indice(x, tab) -> int:
    '''Retourne l'indice du premier x dans tab.
    Données
        tab : list tableau d'entiers
        x   : int valeur à chercher
    Sorite
        ind : int, indice de x dans tab,
        -1 sinon
    Exemples
    >>> indice(0, []) == -1
    True
    >>> indice(0, [0, 5, 8]) == 0
    True
    '''
    ind = -1 # x n'est pas trouvés
    for i, elm in enumerate(tab):
        if elm == x:
            ind = i
            break
    return ind
##
def compter(x, tab) -> int:
    '''Retourne le nombre d'occurrences x dans tab.
    Données
        tab : list tableau d'entiers
        x   : int valeur à chercher
    Sorite
        cpt : int, compteur des x dans tab,
    Exemples
    >>> compter(0, []) == 0
    True
    >>> compter(0, [0, 5, 8]) == 1
    True
    '''
    cpt = 0
    for elm in tab:
        if elm == x:
            cpt += 1
    return cpt
##
def min(tab) -> int:
    '''Retourne le minimum d'un tab.
    Données
        tab: list, tableau d'entiers
    Sorite
        mn : int, valeur minimale
    Exemples
    >>> min([0, 5, 8]) == 0
    True
    '''
    mn = tab[0] # minimum provisoire
    for i in range(1, len(tab)):
        if tab[i] < mn:
            mn = tab[i]
    return mn

##
def max(tab) -> int:
    '''Retourne le maximum d'un tableau.
    Données
    -------
        tab: list, tableau d'entiers
    Sorite
    ------
        mx : int, valeur maximale
    Exemples
    --------
    >>> max([0, 5, 8]) == 8
    True
    '''
    assert len(tab) > 0, 'Tabbleau vide'
    mx = tab[0]         # maximum provisoire
    for i in range(1, len(tab)):
        if tab[i] > mx:
            mx = tab[i] # maximum provisoire
    return mx
    
t = [1, 2, 2, 5, 2,]
x = 2

resultat = indice(x, t)
print(resultat)