'''Algorithmes de base : Manipulation des tableaux à une dimension.

A. MHAMEDI

LYDEX 2017/18

Objectifs:

    1. Comment parcourir un tableau? accès aux éléments
    2. Comment construir un résultat petit à petit? méthode incrémentale
    3. Comment rechercher un élément dans un tableau? méthode de recherche
'''


## PARCOURS : Lecture
def saisie(tab):
    taille = len(tab)  # variable locale
    print('Vous allez saisir', taille, 'valeurs')
    for i in range(taille):
        tab[i] = eval(input('\n\t tab['+str(i)+'] = ? '))


## PARCOURS : Ecriture
def affichage(tab):
    taille = len(tab)
    print('Affichage de ', taille, 'valeurs ')
    for i in range(taille):
        print('tab[', i, '] = ', tab[i], sep='', end='; ')


## METHODE INCREMENTALE : Somme
def somme(Notes) -> float:
    '''Calcule la somme des notes.
	
    Données:
    :param: Notes : list, tableaux des notes
    :param: taille: int, nombre des notes
    :param: indice: int, indice d'une note dans le tableau
    Sortie:
    :return: somme : float, somme des notes.
    Exemples:

    >>> somme([15.2, 14.75, 20.0])
    49.95
    '''
    taille = len(Notes)
    # Méthode incrémentale :
    somme = 0                       # 1. Initialisation du résultat
    for indice in range(taille):
            somme += Notes[indice]  # 2. Construction du résultat
    return somme                    # 3. Renvoi du résultat final


## Moyenne
def moyenne(Notes) -> float:
    '''Calcule la moyenne des notes.
    Données:
    
        Notes : list, tableaux des notes
        taille: int, nombre des notes
        som : float, somme des notes.
    Sortie:
    
        moy : float, moyenne des notes.
    Exemples:

    >>> moyenne([15.25, 17.50, 19.0])
    17.25
    '''
    taille = len(Notes)
    som = somme(Notes)
    moy = som / taille
    return moy


## RECHERCHE : Appartenance
def appartient(x, tab) -> bool:
    '''Teste si x fait partie de tab.
    Données
    
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
    for elm in tab:         # PARCOURS
        if elm == x:        # COMPARAISON
            trouve = True
            break
    return trouve


## RECHERCHE : Indice
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
    ind = -1  # x n'est pas trouvés
    for i, elm in enumerate(tab):  # PARCOURS
        if elm == x:               # COMPARAISON
            ind = i
            break
    return ind


## RECHERCHE : Comptage
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
    for elm in tab:         # PARCOURS
        if elm == x:        # COMPARAISON
            cpt += 1
    return cpt


## RECHERCHE : Minimum
# Attention une fonction pédéfinie min existe déjà sera remplacée.
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
    mn = tab[0]  # minimum provisoire
    for i in range(1, len(tab)):    # PARCOURS
        if tab[i] < mn:             # COMPARAISON
            mn = tab[i]
    return mn


## RECHERCHE : Maximum
# Attention une fonction pédéfinie max existe déjà sera remplacée.
def max(tab) -> int:
    '''Retourne le maximum d'un tableau.
	
    Données
    
        tab: list, tableau d'entiers
    Sorite
    ------
        mx : int, valeur maximale
    Exemples

    >>> max([0, 5, 8]) == 8
    True
    '''
    assert len(tab) > 0, 'Tableau vide'
    mx = tab[0]          # maximum provisoire
    for i in range(1, len(tab)):
        if tab[i] > mx:
            mx = tab[i]  # maximum provisoire
    return mx


##
def SommeTab(A, B):
    Na = len(A)
    Nb = len(B)
    assert Na == Nb, 'Données non valides'
    somAB = []
    for i in range(Na):
        somAB += [A[i] + B[i]]
    return somAB

	
# PROGRAMME PRINCIPAL
if __name__ == '__main__':
	A = [15.2, 14.75, 20.0]
	resultat = somme(A)
	print('La somme est :', resultat)
	taille = 5  # variable globale
	A = [0] * taille
	saisie(A)
	affichage(A)
	t = A
	x = eval(input('Entrer une valeur : '))
	resultat = appartient(x, t)
	print(x, 'appartient au tableau ?', resultat)
	resultat = indice(x, t)
	print('L\'indice de', x, 'est', resultat)
	resultat = compter(x, t)
	print('Le nombre d\'occurrences de', x, 'est', resultat)
	# Appel
	resultat = min(t)
	print('Le minimum est', resultat)
	resultat = max(t)
	print('Le maximum est', resultat)
	resultat = SommeTab(t, t)
	print('La Somme est', resultat)
