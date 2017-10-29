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
    
    # Appel
    taille = 5
    A = [0] * taille
    saisie(A)


Affichage
"""""""""
.. code-block:: python

    def affichage(tab):
        taille = len(tab)
        print('Affichage de ', taille, 'valeurs ')
        for i in range(taille):
            print('tab[', i, '] = ', tab[i], sep='', end='; ')
    
    # Appel
    A = [1, 2, 3, 4, 5, 8]
    affichage(A)





Recherche dans un tableau
-------------------------
Recherche de la premi�re occurrence
"""""""""""""""""""""""""""""""""""
Compter toutes les occurrences
""""""""""""""""""""""""""""""
Minimum d'un tableau
""""""""""""""""""""
Maximum d'un tableau
""""""""""""""""""""
Op�rations sur les tableaux
---------------------------
Somme des �l�ments
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