"""Tp6 : titre.
##############
Objectifs
-----------
    #. Manipuler les fichiers et les chaînes de caractères.
    #. Appliquer l'analyse déscendente.
"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'


def time2seconds(time: str) -> int:
    """Transforme le temps en secondes.

    permet de calculer le temps et la durée en secondes.
    """
    if ':' in time:
        h, m, s = time.split(':')
    else:
        h = 0
        m, s = time.rstrip('s').split('min ')
    s = int(s)
    m = int(m)
    h = int(h)
    temps = h * 60 ** 2 + m * 60 + s
    return temps


def datetuple(dt: str) -> tuple:
    """Convertit une str en tuple d'entiers.

    Parameters
    ----------
    dt
        date sous la forme jj/mm/aaaa
    Returns
    -------
    date
        date sous forme de tuple d'entiers

    Examples
    --------

    >>> datetuple('12/12/2017')
    (12, 12, 2017)
    """
    j, m, a = map(int, dt.split('/'))
    return j, m, a


def format(temps:int, duree: bool) -> str:
    """Formatte le temps.

    99mins 99s pour la durée.
    00:00:00 pour le temps.
    """
    m = temps // 60
    s = temps % 60
    msg = '%0dmin %0ds'
    data = m, s
    j = (m // 60) // 24
    if not duree:
        h = (m // 60) % 24
        m %= 60
        data = h, m, s
        msg = '%0d:%0d:%0d'
    return msg % data, j

def filtrer(**criteres):
    pass


def tempsdefin(date, temps, duree):
    temps = time2seconds(temps)
    duree = time2seconds(duree)
    heurefin, jourok = format(temps + duree, False)
    # date = datesuivante(*datetuple(date)) if jourok else date
    date = "Le lendemain" if jourok else "le jour même"
    return date, heurefin


def analyser(contenu) -> list:
    """Analyse le contenu du fichier appels.csv.
    """
    l_contenu = contenu.split('\n')
    titres = l_contenu[0].split(';')
    # print(titres)
    ll_contenu = []
    for i in range(1, len(l_contenu)):
        appel = l_contenu[i].split(';')
        ll_contenu.append(appel)
    return ll_contenu


def etendre(ll_contenu: list):
    for i in range(len(ll_contenu)):
        date, temps, duree = ll_contenu[i][1:]
        date = tempsdefin(date, temps, duree)
        ll_contenu[i].extend(date)

def backtotext(ll_contenu) -> str:
    for i in range(len(ll_contenu)):
        ll_contenu[i] = ';'.join(ll_contenu[i])
    return '\n'.join(ll_contenu)


if __name__ == '__main__':
    import td7.td7_2sol as td7
    # VARIABLES GLOBALES
    path = 'appels.csv'
    code = 'utf-8'
    with open(path, encoding=code) as gf:
        contenu = gf.read().strip()

    listeDesAppels = analyser(contenu)
    etendre(listeDesAppels)
    print(backtotext(listeDesAppels))
