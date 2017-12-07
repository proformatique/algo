"""TP4 : chaînes de caractères.

Objectifs :

    #. Compter tous les occurrences de chaque caractère d'un texte
    #. Utiliser les listes et les chaînes (lien logique i)
    #. Supprimer les doublons d'un texte (nouvelle copie)
"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'

from TD5.td5_sol import indice


def inverser(texte: str) -> str:
    """Retourne une version de texte à l'envers

    Parameters
    ----------
    texte : str
        texte source
    Retruns
    -------
    copie : str
        texte à l'envers
    Examples
    --------
    >>> inverser('s.o.s')
    's.o.s'
    >>> inverser('matplotlib')
    'biltolptam'
    """
    copie = ''
    for car in texte:
        copie = car + copie
    return copie


def remplacer(mot1:str, mot2:str, texte: str) -> str:
    """Retourne une version de texte avec mot2 au lieu de mot1

    Parameters
    ----------
    texte : str
        texte source
    mot1 : str
        mot à remplacer
    Retruns
    -------
    mot2 : str
        mot de remplacement
    Examples
    --------
    >>> remplacer('im', '', 'impossible')
    'possible'
    >>> remplacer('', '', 'possible')
    'possible'
    """
    copie = ''
    for car in texte:
        copie = car + copie
    return copie


def rotation(mot1: str, mot2: str) -> bool:
    """Vérifie si le mot2 est une rotation de mot1.
    
    """

if __name__ == "__main__":
    import doctest as dt
    dt.testmod()
