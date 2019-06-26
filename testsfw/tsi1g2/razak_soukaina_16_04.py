# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:30:01 2018

@author: Lydex
"""

def recherche (nom_du_fichier , mot_a_chercher)->list:
    R=[]
    cpt=0 
    with open(nom_du_fichier , mot_a_chercher)as f:
        data = f.read().split('\n')
        for line in data:
         if mot_a_chercher in line:
             R+=[cpt]
         cpt += 1
        else:
           return line
   
           