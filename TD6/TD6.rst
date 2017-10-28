***********
Tableaux 1D
***********
Algorithmes de base
===================
Parcourir un tableau
--------------------
Saisie
""""""
.. code-block:: python

    def saisie(tab):
        taille = len(tab)
        print('Vous allez saisir', taille, 'valeurs')
        for i in range(taille):
            tab[i] = eval(input('\n\t tab['+str(i)+'] = ? '))


Affichage
"""""""""
.. code-block:: python

    def affichage(tab):
        taille = len(tab)
        print('Affichege de ', taille, 'valeurs ')
        for i in range(taille):
            print('tab[', i, '] = ', tab[i], end='; ')




Recherche dans un tableau
-------------------------
Recherche de la première occurrence
"""""""""""""""""""""""""""""""""""
Compter toutes les occurrences
""""""""""""""""""""""""""""""
Minimum d'un tableau
""""""""""""""""""""
Maximum d'un tableau
""""""""""""""""""""
Opérations sur les tableaux
---------------------------
Somme des éléments
""""""""""""""""""
Somme de deux tableaux
""""""""""""""""""""""
Permutation
"""""""""""
Permutation circulaire
""""""""""""""""""""""
Inverse
"""""""
***********
Tableaux 2D
***********