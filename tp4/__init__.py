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

__version__ = '0.1'
__author__ = 'A. MHAMEDI'



# Parcours
def palindrome(texte: str) -> bool:
    """Retourne True si texte se lit des deux sens par ex. s.o.s.
    
    Parameters
    ----------
    texte:
        texte source à vérifier.
    
    Returns
    -------
    pal :
        True si le texte est un palindrome, sinon False.

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
    texte :
        texte source

    Returns
    -------
    copie :
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
    texte :
        texte source
    mot1 :
        mot à remplacer
    mot2 :
        mot de remplacement
    
    Returns
    -------
    copie: str
        texte modifié
    
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
        if n and mot1 == texte[i:i + n]: # lazy evaluation
            copie += mot2
            i += n # si n == 0 boucle infinie
            # i += n if n > m else m # pour la forme des cartes
        else:
            copie += texte[i]
            i += 1
    return copie


# Recherche
def estrotation(mot1: str, mot2: str) -> bool:
    """Vérifie si le mot2 est une rotation de mot1.
    
    :param mot1: premier mot
    :param mot2: deuxième mot

    Examples
    --------
    >>> estrotation('abcde', 'cdeab')
    True
    """
    return len(mot1) == len(mot2) and mot1 in mot2 * 2

def estrotation2(mot1: str, mot2: str) -> bool:
    """Vérifie si le mot2 est une rotation de mot1.
    
    :param mot1: premier mot
    :param mot2: deuxième mot

    Examples
    --------
    >>> estrotation2('abcde', 'cdeab')
    True
    """
    # return len(mot1) == len(mot2) and mot1 in mot2 * 2
    i = 0
    n = len(mot1)
    m = len(mot2)
    while i < n:
        j = 0
        while j < n and mot1[j] == mot2[(i + j) % n]:
            j += 1
        if j == n:
            return True
        i += 1
    return False

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
            if 'nom' in ligne: # premiere ligne
                motsaremplacer = ligne.split()
                continue
            remplacants = ligne.split() # le reste des lignes
            contact = contacts
            for i in range(len(motsaremplacer)):
                mot1 = motsaremplacer[i]
                mot2 = remplacants[i]
                contact = remplacer(mot1, mot2, contact)
            print(contact, '\n' * 2)
