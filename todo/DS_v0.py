# DS
def  jour(pj, j):
    '''Affiche le nom du jour j.
    Parameters
    -----------
    j : int: jour à afficher
    pj: int: premier jour du mois
    jours : list, les jours de la semaine
    Returns
    -------
    nomdujour : str, nom du jour demandé
    >>> jour(7, 2) # le mois commence par un Dimanche, le 2em jour est Lundi
    'Lundi'
    '''
    assert 1 <= pj <= 7 and 1 <= j <= 31, 'Données non valides'
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    nomdujour = jours[(j + pj - 2) % 7]
    return nomdujour


def extremum(meteo, mesure, max):
    '''Affiche le nom du jour j.
    Parameters
    -----------
    mesure : int
        0 et 1 température, 2 précipitations
    meteo : list
        tableau des données enregistrées pendant un mois.
    Returns
    -------
    minim : float
        valeur minimale
    >>> extremum(meteo, 0, False) # minimum des températures minimales
    >>> extremum(meteo, 1, True)  # maximum des températures maximales
    '''
    assert 0 <= mesure <= 2
    ext = meteo[mesure][0]
    for i in range(len(meteo[mesure])):
        dt = meteo[mesure][i]
        condition = dt > ext if max else dt < ext
        if (condition):
            ext = dt
    return ext


def recherche(meteo, mesure, valeur):
    for i in range(len(meteo[mesure])):
        dt = meteo[mesure][i]
        condition = dt == valeur
        if (condition):
            jour = i + 1
    return jour


def cumul(meteo, mesure):
    cu = []
    som = 0
    for i in range(len(meteo[mesure])):
        som += meteo[mesure][i]
        cu += [som]
    return cu


def rechercheMax(meteo):
    valeur = meteo[1][0] - meteo[0][0]
    jour = 1
    for i in range(1, len(meteo[0])):
        dt = meteo[1][i] - meteo[0][i]
        condition = dt > valeur
        if (condition):
            jour = i + 1
            valeur = dt
    return jour


def afficher(meteo, pj):
    for i in range(len(meteo)):
        print(jour(pj, i + 1) + ' : ' + str(i + 1) + "/01/2017 Cumul", meteo[i])
#          0    1    2    3    4    5    6    7    8    9     10   11   12   13   14   15
Tempmin = [4.2, 3.8, 4.0, 5.0, 4.4, 4.3, 5.6, 5.9, 4.7, 4.7,  5.3, 4.8, 5.1, 7.5, 4.9, 3.3,
           2.1, 3.7, 7.6, 3.5, 2.5, 2.2, 1.5, 3.2, 2.1, 1.2, 10.9, 7.5, 6.5, 6.2, 7.2]
Tempmax = [19.4, 20.3, 21.7, 22.9, 21.6, 21.4, 22.2, 18.9, 20.8, 18.4, 19.1, 21.0, 18.8, 15.3, 17.2,
           18.7, 18.0, 16.1, 14.2, 12.9, 11.2, 13.7, 13.8, 14.5, 17.4, 21.0, 17.9, 19.8, 23.2, 23.8, 20.5]
Precip  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.0, 0, 0, 3.0, 0, 0, 0,
           0, 0, 0, 1.0, 0, 0]
#               0        1        2
meteo = [Tempmin, Tempmax, Precip]
premierjour = 7
mesure = 0
max = extremum(meteo, mesure, True)
min = extremum(meteo, mesure, False)
jourmx = recherche(meteo, mesure, max)
jourmn = recherche(meteo, mesure, min)
print('Le maximum de la température minimale ', max,' a été enregisré', jour(premierjour, jourmx),' le', jourmx, '/01/2017')
print('Le minimum de la température minimale ', min,' a été enregisré ', jour(premierjour, jourmn), 'le', jourmn, '/01/2017')
mesure = 1
max = extremum(meteo, mesure, True)
min = extremum(meteo, mesure, False)
jourmx = recherche(meteo, mesure, max)
jourmn = recherche(meteo, mesure, min)
jourMax = rechercheMax(meteo)
print('Le maximum de la température maximale ', max,' a été enregisré', jour(premierjour, jourmx),' le', jourmx, '/01/2017')
print('Le minimum de la température maximale ', min,' a été enregisré ', jour(premierjour, jourmn), 'le', jourmn, '/01/2017')
print('L\'amplitude maximale a été enregisrée ', jour(premierjour, jourMax), 'le', jourMax, '/01/2017')
mesure = 2
afficher(cumul(meteo, mesure), premierjour)
