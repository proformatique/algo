# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def recherche(nom_du_fichier, mot_a_chercher):
    """Rechercher les lignes qui comportent un mot donné"""
    try:
        L=[]
        with open(nom_du_fichier,mode="r",encoding="utf-8") as f:
            for i, line in enumerate(f):
                if mot_a_chercher in line:
                    L+=[i+1]
                    return L
    except:
        return []

def inserer(tab, element):
    """Insérer un élément dans un tableau par dichotomie récursive"""
    
    try:
    
        if len(tab)==0:
            return [element]
        c=(len(tab))//2
        m=tab[c]
        if element<m:
            return inserer(tab[:c],element)+tab[c:]
        else:
            return tab[:c+1]+inserer(tab[c+1:],element)
    except:
        return tab
    