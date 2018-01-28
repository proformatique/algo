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


def formater(temps: int, duree: bool) -> str:
    """Formate le temps.

    Note
    ----
    99mins 99s pour la durée.
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
    msg = '%02dmin %02ds'
    data = minutes, secondes
    jours = (minutes // 60) // 24
    if not duree:
        heure = (minutes // 60) % 24
        minutes %= 60
        data = heure, minutes, secondes
        msg = '%02d:%02d:%02d'
    return msg % data, jours


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
    datedefin: str
    jourok: int
    """
    temps = tempsensecondes(temps)
    duree = tempsensecondes(duree)
    heurefin, jourok = formater(temps + duree, False)
    # date = datesuivante(*datetuple(date)) if jourok else date
    datedefin = "Le lendemain" if jourok else date
    return datedefin, heurefin


def analyser(contenu) -> list:
    """Analyse le contenu du fichier appels.csv.
    """
    l_contenu = contenu.split('\n')
    # titres = l_contenu[0].split(';')
    # print(titres)
    ll_contenu = []
    for i in range(1, len(l_contenu)):
        appel = l_contenu[i].split(';')
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
        date, temps, duree = ligne[1:]
        date = tempsdefin(date, temps, duree)
        del ll_contenu[i][3]
        ll_contenu[i].extend(date)


def backtotext(ll_contenu: list) -> str:
    """
    Transforme la liste de listes en chaîne de caractères.

    Parameters
    ----------
    ll_contenu:
        résultat sous forme de liste de listes
    """
    for i, ligne in enumerate(ll_contenu):
        ll_contenu[i] = ';'.join(ligne)
    return '\n'.join(ll_contenu)


if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
    # VARIABLES GLOBALES
    PATH = 'appels.csv'
    DEST = 'data.csv'
    CONTENUTXT = charger(PATH)
    LISTEDESAPPELS = analyser(CONTENUTXT)
    etendre(LISTEDESAPPELS)
    RESULTAT = backtotext(LISTEDESAPPELS)
    enregistrer(RESULTAT, DEST)
