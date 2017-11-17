# DS
def  jour(pj, j):
    '''Affiche le nom du jour j.
    Données
    -------
    j : int: jour à afficher
    pj: int: premier jour du mois
    jours : list, les jours de la semaine
    Sortie
    ------
    nomdujour : str, nom du jour demandé
    >>> jour(7, 2) # le mois commence par un Dimanche, le deuxième jour est Lundi
    'Lundi'
    '''
    assert 1<= pj <= 7 and 1 <= j <=31, 'Données non valides'
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
#Todo complétez le code
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,... 
    nomdujour = jours[(j+pj-2)% 7]
    return nomdujour

def extremum(donneesMeteo, mesure, max):
    '''Affiche le nom du jour j.
    Données
    -------
    mesure : int, 0 et 1 température, 2 précipitations
    donneesMeteo : list: tableau des données enregistrées pendant un mois.
    Sortie
    ------
    minim : float, valeur minimale
    >>> extremum(donneesMeteo, 0, False) # minimum des températures minimales
    >>> extremum(donneesMeteo, 1, True)  # maximum des températures maximales
    '''
    assert 0 <= mesure <= 2
#Todo complétez le code
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...
    ext = donneesMeteo[mesure][0]
    for i in range(len(donneesMeteo[mesure])):
        dt = donneesMeteo[mesure][i]
        condition = dt > ext if max else dt < ext
        if (condition):
            ext = dt
    return ext
    
def recherche(donneesMeteo, mesure, valeur):
#Todo complétez le code
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...
    for i in range(len(donneesMeteo[mesure])):
        dt = donneesMeteo[mesure][i]
        condition = dt == valeur
        if (condition):
            jour = i + 1
    return jour

def cumul(donneesMeteo, mesure):
#Todo complétez le code
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...
    cu = []
    som = 0 
    for i in range(len(donneesMeteo[mesure])):
        som += donneesMeteo[mesure][i]
        cu += [som]
    return cu

def rechercheMax(donneesMeteo):
#Todo complétez le code
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...,
    ...,...,...,...,...,...,...,...,...,...
    valeur = donneesMeteo[1][0] - donneesMeteo[0][0]
    jour = 1
    for i in range(1, len(donneesMeteo[0])):
        dt = donneesMeteo[1][i] - donneesMeteo[0][i]
        condition = dt > valeur
        if (condition):
            jour = i + 1
            valeur = dt
    return jour

def afficher(donneesMeteo, pj):
    for i in range(len(donneesMeteo)):
        print(jour(pj, i+1)+' : ' + str(i+1)+ "/01/2017 Cumul", donneesMeteo[i])
#          0    1    2    3    4    5    6    7    8    9     10   11   12   13   14   15
Tempmin = [4.2, 3.8, 4.0, 5.0, 4.4, 4.3, 5.6, 5.9, 4.7, 4.7,  5.3, 4.8, 5.1, 7.5, 4.9, 3.3,
           2.1, 3.7, 7.6, 3.5, 2.5, 2.2, 1.5, 3.2, 2.1, 1.2, 10.9, 7.5, 6.5, 6.2, 7.2]
Tempmax = [19.4, 20.3, 21.7, 22.9, 21.6, 21.4, 22.2, 18.9, 20.8, 18.4, 19.1, 21.0, 18.8, 15.3, 17.2,
           18.7, 18.0, 16.1, 14.2, 12.9, 11.2, 13.7, 13.8, 14.5, 17.4, 21.0, 17.9, 19.8, 23.2, 23.8, 20.5]
Precip  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.0, 0, 0, 3.0, 0, 0, 0,
           0, 0, 0, 1.0, 0, 0]
#               0        1        2
donneesMeteo = [Tempmin, Tempmax, Precip]    
premierjour = 7
mesure = 0
max = extremum(donneesMeteo, mesure, True)
min = extremum(donneesMeteo, mesure, False)
jourmx = recherche(donneesMeteo, mesure, max)
jourmn = recherche(donneesMeteo, mesure, min)
print('Le maximum de la température minimale ', max,' a été enregisré', jour(premierjour, jourmx),' le', jourmx, '/01/2017')
print('Le minimum de la température minimale ', min,' a été enregisré ', jour(premierjour, jourmn), 'le', jourmn, '/01/2017')
mesure = 1
max = extremum(donneesMeteo, mesure, True)
min = extremum(donneesMeteo, mesure, False)
jourmx = recherche(donneesMeteo, mesure, max)
jourmn = recherche(donneesMeteo, mesure, min)
jourMax = rechercheMax(donneesMeteo)
print('Le maximum de la température maximale ', max,' a été enregisré', jour(premierjour, jourmx),' le', jourmx, '/01/2017')
print('Le minimum de la température maximale ', min,' a été enregisré ', jour(premierjour, jourmn), 'le', jourmn, '/01/2017')
print('L\'amplitude maximale a été enregisrée ', jour(premierjour, jourMax), 'le', jourMax, '/01/2017') 
mesure = 2
afficher(cumul(donneesMeteo, mesure), premierjour)
   
