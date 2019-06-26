# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:25:51 2018

@author: Lydex
"""

def recherche(nom_du_fichier,mot_a_chercher):
    """
    >>> recherche('python.txt','maison')
    [1, 2, 4]
    
    """
    L=[]
    l=1
    with open(nom_du_fichier,'r') as f:
        while f.readline() != '':
            A=f.readline()
            if ' mot_a_chercher ' in A:
                L=L+[l]
            l=l+1
    return L

def inserer(tab,element):
    if tab==[]:
        return [element]
    elif element <= tab[O]:
        return [element] + tab
    elif element >= tab[-1]:
        return tab + [element]
    else:
        b=0
        for i in range(len(tab)):
            if tab[i] <l and tab[i+1] >= l :
                b=i
        tab.insert(b,element)
        return tab

if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
        