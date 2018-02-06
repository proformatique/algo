from temps import tempsdefin
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
            del ll_contenu[i][3]  # supprime la durée.
            ll_contenu[i].extend(datetpl)  # ajoute les éléments du tuple.


def backtotext(ll_contenu: list) -> str:
    """Transforme la liste de listes en chaîne de caractères.

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

def analyser(contenu: str) -> list:
    """Analyse le contenu du fichier appels.csv.

    Retourne un tableau à 2d de tous les champs.

    Parameters
    ----------
    contenu:
        texte à analyser.

    Returns
    -------
    ll_contenu: list

    Note
    -----
    Application de la méthode incrémentale
    """
    l_contenu = contenu.split('\n')
    ll_contenu = []
    for ligne in l_contenu:
        appel = ligne.split(';')
        ll_contenu.append(appel)
    return ll_contenu

