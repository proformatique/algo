# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:30:01 2018

@author: Lydex
"""

def rechercher(fichier, mot):
    liste = []
    cpt = 0
    try:
        with open(fichier) as f:
            for i in f:
                cpt += 1
                if mot in i:
                    liste.append(cpt)
    finally:
        return liste

def inserer(tab, element):
    if len(tab) == 0:
        tab = [element]
        return tab
    else:
        try:
            assert isinstance(element, type(tab[0]))
        except:
            print('Veuillez inserer un element du type : {}'.format(type(tab[0])))
        else:
            if element <= tab[0]:
                tab = [element]+tab
            else:
                tab = [tab[0]] + inserer(tab[1:], element)
        finally:
            return tab
            