"""Module
Objectifs :
    #.
    #.
    #.
"""
__author__ = 'A. MHAMEDI'          
__version__ = '0.1'

def compter(texte) -> list:
    """Compte les caractères d'un texte."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    compteurs = [0] * len(alphabet)
    for caractere in texte:
        if caractere in alphabet:
            i = alphabet.index(caractere)
            compteurs[i] += 1

    




if __name__ == "__main__":
    import doctest as dt
    dt.testmod()