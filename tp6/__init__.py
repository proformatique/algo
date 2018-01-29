"""
Tp6 - Chaînes de caractères & fichiers
======================================

Objectifs:
    #. Manipuler les fichiers de données.
    #. Manipuler les chaînes de caractères.
"""


__author__ = 'A. MHAMEDI'
__version__ = '0.1'


def charger(fichier: str) -> str:
    '''Charge le fichier spécifié.

    Parameters
    ----------
    fichier :
        nom du fichier texte.

    Returns
    -------
    texte : contenu du fichier texte.
    '''
    with open(fichier, encoding='utf-8') as file2read:
        texte = file2read.read()
        return texte.strip()


def enregistrer(texte: str, fichier: str):
    '''Enregistre le texte dans le fichier spécifié.

    Parameters
    ----------
    texte :
        contenu du fichier à enregistrer.
    fichier :
        nom du fichier texte.

    '''
    with open(fichier, mode='w', encoding='utf-8') as file2save:
        file2save.write(texte)


def tempsensecondes(temps: str) -> int:
    """Transforme le temps en secondes.

    permet de calculer le temps et la durée en secondes.

    Parameters
    ----------
    temps:
        temps ou durée.

    Returns
    -------
    tempsensec: temps en secondes
    """
    if ':' in temps:
        heures, minutes, secondes = temps.split(':')
    else:
        heures = 0
        minutes, secondes = temps.rstrip('s').split('min ')
    heures, minutes, secondes = map(int, [heures, minutes, secondes])
    tempsensec = heures * 60 ** 2 + minutes * 60 + secondes
    return tempsensec


def datetuple(date: str) -> tuple:
    """Convertit une str en tuple d'entiers.

    Parameters
    ----------
    date:
        date sous la forme jj/mm/aaaa
    Returns
    -------
    datetpl: date sous forme de tuple d'entiers

    Examples
    --------

    >>> datetuple('12/12/2017')
    (12, 12, 2017)
    """
    jour, mois, annee = map(int, date.split('/'))
    datetpl = jour, mois, annee
    return datetpl


def formater(temps: int, duree: bool) -> tuple:
    """Formate le temps.

    Note
    ----
    00mins 00s pour la durée.
    00:00:00 pour le temps.

    Examples
    --------
    >>> formater(2165, True)
    ('36min 05s', 0)
    >>> formater(2165, False)
    ('00:36:05', 0)
    >>> formater(32165, False)
    ('08:56:05', 0)
    """
    
    minutes = temps // 60
    secondes = temps % 60
    heures = minutes // 60
    jours = heures // 24
    if duree:
        forme = '%02dmin %02ds'
        data = minutes, secondes
    else:
        minutes %= 60
        heures %= 24
        forme = '%02d:%02d:%02d'
        data = heures, minutes, secondes
    return forme % data, jours


def tempsdefin(date: str, temps: str, duree: str) -> tuple:
    """Calcule la date de fin.

    La date et l'heure après la conversation.
    
    Parameters
    ----------
    date:
        sous la fome jj/mm/aaaa.
    temps:
        sous la forme HH:MM:SS.
    duree:
        sous la forme 00min 00s.
    Returns
    -------
    tempsdefin: str
    jourok: int
    """
    temps = tempsensecondes(temps)
    duree = tempsensecondes(duree)
    heurefin, jourok = formater(temps + duree, False)
    # datedefin = datesuivante(*datetuple(date)) if jourok else date
    datedefin = "Le lendemain" if jourok else date
    return datedefin, heurefin


def analyser(contenu: str) -> list:
    """Analyse le contenu du fichier appels.csv.
    
    Retourne un tableau à 2d de tous les champs.
    Parameters
    ----------
    contenu:
        texte à analyser.
    """
    l_contenu = contenu.split('\n')
    ll_contenu = []
    for ligne in l_contenu:
        appel = ligne.split(';')
        ll_contenu.append(appel)
    return ll_contenu


def etendre(ll_contenu: list):
    """Remplace la durée par le temps et date de fin dans la liste.

    Parameters
    ----------
    ll_contenu:
        Données du fichiers apples.csv sous forme de liste de listes.
    """
    for i, ligne in enumerate(ll_contenu):
        if i == 0:
            ligne = ligne[:-1] + ['Date de fin', 'Temps de fin']
            ll_contenu[i] = ligne
        else:
            date, temps, duree = ligne[1:]
            datetpl = tempsdefin(date, temps, duree)
            del ll_contenu[i][3]
            ll_contenu[i].extend(datetpl)
    return ll_contenu


def backtotext(ll_contenu: list) -> str:
    """
    Transforme la liste de listes en chaîne de caractères.

    Parameters
    ----------
    ll_contenu:
        résultat sous forme de liste de listes
    """
    sepchamps = ';'
    seplignes = '\n'
    for i, ligne in enumerate(ll_contenu):
        ll_contenu[i] = sepchamps.join(ligne)
    return seplignes.join(ll_contenu)


if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
    # VARIABLES GLOBALES
    PATH = 'appels.csv'
    DEST = 'data.csv'
    contenutexte = charger(PATH)
    listedesappels = analyser(contenutexte)
    listedesappels = etendre(listedesappels)
    contenutexte = backtotext(listedesappels)
    enregistrer(contenutexte, DEST)
