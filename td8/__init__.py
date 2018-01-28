# -*- coding: utf-8 -*-
"""Td8 : chaînes de caractères.

Objectifs :

    #. Compter toutes les occurrences de chaque caractère d'un texte
    #. Utiliser les listes et les chaînes (lien logique par indice)
    #. Supprimer les doublons d'un texte (nouvelle copie)
"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'

from td5.td5_sol import indice


def comptertout0(texte) -> list:
    """Compter le nombre d'occurrences de chaque lettre.

    >>> comptertout0('texte' * 3)
    [6, 6, 3]
    """
    # Première tentative
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    compteurs = [0] * len(alphabet)
    for caractere in texte:
        if caractere in alphabet:
            i = alphabet.index(caractere)
            compteurs[i] += 1
    return compteurs


def comptertout1(texte) -> list:
    """Compte les caractères d'un texte.

    Examples
    --------
    >>> comptertout1('texte' * 3)
    [6, 6, 3]
    """
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = texte
    compteurs = [0] * len(alphabet)
    for caractere in texte:
        # i = texte.index(caractere)
        i = indice(caractere, alphabet)
        compteurs[i] += 1
    return compteurs


def sansdoublons(texte: str) -> str:
    """Retourne une version sans doublons de texte.

    Parameters
    ----------
    texte: str
        texte source

    Returns
    -------
    copie : str
        texte sans doublons

    Examples
    --------
    >>> sansdoublons('texte')
    'tex'
    >>> sansdoublons('matplotlib')
    'matploib'
    """
    copie = ''
    for car in texte:
        if car not in copie:
            copie += car
    return copie


def comptertout(texte: str) -> list:
    """Compte le nombre d'occurrences de chaque lettre dans un *texte*.

    Parameters
    ----------
    texte : str
        texte de départ

    Returns
    -------
    compteurs : list des int
        liste des compteurs

    Examples
    --------
    >>> comptertout('texte' * 3)
    [6, 6, 3]

    See Also
    --------
    td5.compter : tableau à une dimension
    td5.indice : indice d'un élément dans un tableau à une dimension
    """
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = sansdoublons(texte)
    # alphabet = sansponctuation(alphabet)
    compteurs = [0] * len(alphabet)
    for caractere in texte:
        # i = texte.index(caractere)
        i = indice(caractere, alphabet)
        compteurs[i] += 1
    return compteurs


def affichertout(texte: str):
    """Permet d'afficher les nombres des occurences des lettres d'un texte.

    Parameters
    ----------
    texte : str
        texte source

    Examples
    --------
    >>> affichertout('texte' * 6)
    t : 12
    e : 12
    x : 6
    """
    tex = sansdoublons(texte)
    compteurs = comptertout(texte)
    # resultat = "%s : %s" % (tex[0], compteurs[0])
    resultat = "{} : {}".format(tex[0], compteurs[0])
    for i in range(1, len(tex)):
        ligne = "\n{} : {}".format(tex[i], compteurs[i])
        resultat += ligne
    print(resultat)


# programme principal
if __name__ == "__main__":
    import doctest as dt
    import matplotlib.pyplot as plt
    
    dt.testmod()
    with open("data1.txt", encoding='utf-8') as fichier:
        contenu = fichier.read()
        affichertout(contenu)
    x = range(len(sansdoublons(contenu)))
    y = comptertout(contenu)
    plt.bar(x, y)
    plt.show()
