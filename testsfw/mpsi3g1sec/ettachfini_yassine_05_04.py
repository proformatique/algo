# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 10:17:36 2018

@author: Lydex
"""

def rle(texte):
    copie=''
    cpt=0
    j=0
    for i in range(len(texte)):
        var=texte[j]
        if texte[i]==var:
            cpt=cpt+1
        else:
            j=i
            cpt=0
    copie=copie+str(cpt)+var
    return copie