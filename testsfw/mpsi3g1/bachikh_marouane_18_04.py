# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:06:58 2018

@author: Lydex
"""

def recherche(nom_du_fichier, mot_a_chercher):
    '''
    recherche('texte.txt', 'def')
    >>>[1,2,4,6]
    '''
    a = []
    n = 0
    with open(nom_du_fichier, encoding = 'utf-8') as f:
        texte = f.read()
        for line in texte:
            n += 1
            if mot_a_chercher in line:
                a += [n]
        return a

def inserer(tab, element):
    '''
    inserer([1,2,3,5,6], 4):
        >>>[1,2,3,4,5,6]
        '''
    if len(tab) == 1:
        if tab[0] < element:
            return tab.append(element)
        else:
            return [element, tab[0]]
    elif len(tab) == 0:
        return [element]
    else:
        if tab[len(tab)//2] < element :
            tab = tab[0: len(tab)//2] + inserer(tab[len(tab)//2:], element)
        else:
            tab = inserer(tab[0: len(tab)//2], element) + tab[len(tab)//2:]
    return tab

import doctest as dt
if __name__ == 'main':
    dt.testmod(verbose = True)