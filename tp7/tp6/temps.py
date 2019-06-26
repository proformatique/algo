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
    00min 00s pour la durée.
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
    heures = minutes // 60
    jours = heures // 24
    secondes = temps % 60
    if duree:
        forme = '%02dmin %02ds'
        data = minutes, secondes
    else:
        minutes %= 60
        heures %= 24  # modulo
        forme = '%02d:%02d:%02d'
        data = heures, minutes, secondes
    return forme % data, jours  # opérateur de formatage.


def tempsdefin(date: str, temps: str, duree: str) -> tuple:
    """Calcule la date de fin.

    La date et l'heure après la conversation.

    Parameters
    ----------
    date:
        sous la fome jj/mm/aaaa.
    temps:
        sous la forme 00:00:00.
    duree:
        sous la forme 00min 00s.
    Returns
    -------
    datedefin: str
    heuredefin: int
    """
    temps = tempsensecondes(temps)
    duree = tempsensecondes(duree)
    heuredefin, jourok = formater(temps + duree, False)
    # datedefin = datesuivante(*datetuple(date)) if jourok else date
    datedefin = "Le lendemain" if jourok else date
    return datedefin, heuredefin
