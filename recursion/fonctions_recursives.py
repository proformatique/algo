# -*- coding: utf-8 -*-
"""Tp : titre.

Objectifs
-----------
    #. Créer des fonctions récursives .
    #. Programmer la factorielle récursive.

"""

__author__ = 'A. MHAMEDI'
__version__ = '0.1'


def factorielle(n):
    """
    Examples
    --------
    >>> factorielle(0)
    1
    >>> factorielle(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


def main():
    print("factorielle(5) = ", factorielle(5))
    anagram('google')


def permutation(mot, chosen, choice):
    if len(chosen) < len(mot):
        for i, car in enumerate(mot):
            if i not in chosen:
                permutation(mot, chosen + [i], choice + car)
    else:
        print(choice)


def anagram(mot: str):
    permutation(mot, [], '')

if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=False)
    main()
