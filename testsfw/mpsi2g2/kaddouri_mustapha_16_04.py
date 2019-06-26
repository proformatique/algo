# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:29:53 2018

@author: mustkad
"""

def recherche(nom_du_fichier,mot_a_chercher) -> list:
    try:
        i=0
        T=[]
        with open(nom_du_fichier,mode='r') as df:
            for line in df:
                i+=1
                if mot_a_chercher in line:
                    T+=[i]
        return T
    except:
        return []

def inserer(tab,element) -> list:
    try:
        if len(tab)==0:
            tab+=[element]
            return tab
        else:
            c=int((len(tab)-1)/2)
            if element <= tab[c]:
                return inserer(tab[:c],element) + tab[c:]
            else:
                return tab[:c+1] + inserer(tab[c+1:],element)
    except:
        return tab