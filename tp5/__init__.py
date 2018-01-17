# -*- coding: utf-8 -*-
"""Tp5 : chaînes de caractères.

Objectifs :

    #. Coder texte en utilisant les codes avautk, k7 et césar
    #. Utiliser les tables de codage (lien logique par indice)
    #. Utiliser Variable globale au lieu de Variable locale
"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'


# variables globales
#indice 00000000001111111111222222
#       01234567890123456789012345
alph = 'abcdefghijklmnopqrstuvwxyz'
code = 'klmnopqrstuvwxyzabcdefghij'
c_k7 = 'xyzabcdefghijklmnopqrstuvw'



def avautk(lettre : str) -> str:
    '''Code une lettre en utilisant le code 'a' vaut 'k' (a->k).
    
    Parameters
    ----------
    lettre:
        caracère à coder.
    
    Returns
    -------
    car:
        code de la lettre.


    Examples
    --------
    >>> avautk('a')
    'k'
    '''
    # variable locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    # code = 'klmnopqrstuvwxyzabcdefghij'
    car = code[alph.index(lettre)]
    return car

def codeavautk(texte: str) -> str:
    '''Code un texte en utilisant le code 'a' vaut 'k'.
    
    Parameters
    ----------
    texte:
        texte à coder.
    
    Returns
    -------
    copie : texte codé.

    Examples
    --------
    >>> codeavautk('a bc')
    'k lm'
    '''
    # variables locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    copie = ''
    for car in texte:
        if car in alph:
            car = avautk(car)
        copie += car
    return copie

def k7(lettre: str) -> str:
    '''Code une lettre en utilisant le
    code k7 (k->7).
    
    Examples
    --------
    >>> k7('k')
    'h'
    '''
    return c_k7[alph.index(lettre)]


def cesar(lettre:str, rot:int)-> str:
    '''Code une lettre en utilisant le code cesar.
    
    '''
    #i = alph.index(lettre)
    i = indice(lettre, alph)
    return alph[(i + rot) % len(alph)]
   
def codecesar(texte: str , rotation: int) -> str:
    '''Code un texte en utilisant césar.
    
    '''
    # variables locales
    copie = ''
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    for car in texte:
        if car in alph:
            car = cesar(car, rotation)
        copie += car
    return copie

def cryptanalyse(texte:str) -> str:
    '''Casse le code en utilisant l'analyse des fréquences.
    '''
    tex = td8.sansdoublons(texte)
    compteurs = td8.comptertout(texte)
    m = max(compteurs)
    car = tex[indice(m, compteurs)]
    rot =  indice('e', alph) - indice(car, alph)
    return codecesar(texte, rot)


if __name__ == '__main__':
    import doctest as dt
    import td8
    from td5.td5_sol import indice
    
    dt.testmod()
    with open('cmessage.txt', encoding='utf-8') as ms:
        ctexte = ms.read()
        texte = cryptanalyse(ctexte)
        print(texte)
        
    
    
