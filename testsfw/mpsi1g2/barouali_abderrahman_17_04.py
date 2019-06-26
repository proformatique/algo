# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:17:00 2018

@author: Lydex
"""

def recherche(nom_du_fichier,mot_a_chercher):
    """
    
    >>> recherche(sanstitre4,cmp)
    

    """
    list=[]
    fichier=open("nom_du_fichier.txt","r")
    lignes=fichier.readlines()
    for i in lignes:
        cmp=0
        if mot_a_chercher in i:
            cmp+=1
            list.append(cmp)
    return list

import doctest as dt
dt.testmode()


def inserer(tab,element):
    if tab=[]:
        tab+=[element]
        return tab
    

    