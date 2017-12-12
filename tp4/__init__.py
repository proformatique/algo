# -*- coding: utf-8 -*-
"""TP4.

Chaînes de caractères.
================================

Objectifs :
-----------
    #. Inverser une chaîne de caractères
    #. Remplacer une chaîne de caractères dans une autre
    #. Supprimer une chaîne de caractères dans une autre
    #. Supprimer les espaces superflues d'une chaîne de caractères
"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'


# Parcours
def palindrome(texte: str) -> bool:
    """Retourne True si texte se lit des deux sens par ex. s.o.s.

    Examples
    --------
    >>> palindrome('S.O.S')
    True
    """
    for i in range(len(texte)//2):
        if texte[i] != texte[~i]:
            return False
    return True


# Copie
def inverser(texte: str) -> str:
    """Retourne une version de texte à l'envers.

    Parameters
    ----------
    texte : str
        texte source

    Returns
    -------
    copie : str
        texte à l'envers

    Examples
    --------
    >>> inverser('s.o.s')
    's.o.s'
    >>> inverser('matplotlib')
    'biltolptam'

    See also
    --------
    tp2.inverser : permutation symétrique
    """
    copie = ''
    for car in texte:
        copie = car + copie
    return copie


def remplacer(mot1: str, mot2: str, texte: str) -> str:
    """Retourne une version de texte avec mot2 au lieu de mot1.

    Parameters
    ----------
    texte : str
        texte source
    mot1 : str
        mot à remplacer
    Returns
    -------
    mot2 : str
        mot de remplacement
    Examples
    --------
    >>> remplacer('im', '', 'impossible')
    'possible'
    >>> remplacer('', '', 'possible')
    'possible'
    >>> remplacer('s', 'S', 'possible')
    'poSSible'
    """
    copie = ''
    i = 0
    n = len(mot1)
    m = len(mot2)
    while i < len(texte):
        if n and mot1 == texte[i:i + n]:
            copie += mot2
            i += m if m > n else n
        else:
            copie += texte[i]
            i += 1
    return copie


# Recherche
def estrotation(mot1: str, mot2: str) -> bool:
    """Vérifie si le mot2 est une rotation de mot1.

    Examples
    --------
    >>> estrotation('abcde', 'cdeab')
    True
    """
    return len(mot1) == len(mot2) and mot1 in mot2 * 2


# Rotation
def rotation(mot: str, decalage: int) -> str:
    """Crée une rotation du mot par un décalage des caractères.

    Examples
    --------
    >>> rotation('abcde', 1)
    'bcdea'
    >>> rotation('abcde', 3)
    'deabc'

    """
    n = len(mot)
    copie = ''
    for i in range(n):
        copie += mot[(i + decalage) % n]
    return copie


def supprimerEspaces(texte: str) -> str:
    """Retourne une version de texte sans espaces superflues.

    Examples
    --------
    >>> supprimerEspaces('     un     texte      ')
    'un texte'
    """
    copie = ''
    return copie


if __name__ == "__main__":
    import doctest as dt
    dt.testmod(verbose=True)

    with open(r'contacts\contacts.ctc', encoding='utf-8') as fictc:
        contacts = fictc.read()

    with open(r'contacts\data.vip', encoding='utf-8') as ficvip:
        for ligne in ficvip:
            if 'nom' in ligne:
                motsaremplacer = ligne.split()
                continue
            remplacants = ligne.split()
            contact = contacts
            for i in range(len(motsaremplacer)):
                mot1 = motsaremplacer[i]
                mot2 = remplacants[i]
                contact = remplacer(mot1, mot2, contact)
            print(contact, '\n' * 2)
