*****************************
Tableaux à une dimension - 1D
*****************************
Algorithmes de base
===================
Parcourir un tableau
--------------------
Le traitement d'un tableau tab nécessite l'accès à ces éléments, pour accéder à un élément il suffit de préciser *l'identifiant* du tablau suivi de *l'indice* de l'élément (indexation : tab[indice]), en python les indices sont des entiers qui commencent de 0.

Le parcours c'est accéder à tous les éléments, opération qui se réalise par la répétion de l'indexation.

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
Recherche de la première occurrence
"""""""""""""""""""""""""""""""""""

.. code-block:: python

    def appartient(x, tab):
        trouve = False
    
    def indice(x, tab):
        ...


Compter toutes les occurrences
""""""""""""""""""""""""""""""

.. code-block:: python

    def compter(x, tab):
        '''Retourne le minimum d'un tab.
            Données
                tab: list, tableau d'entiers
                x : int, valeur à compter
            Sorite
                nombre : int, nombre d'occurences de x dans tab
            Exemples
            >>> compter(0, [0, 5, 8, 0]) == 2
            True
        '''
        nombre = 0
    
Minimum d'un tableau
""""""""""""""""""""
.. code-block:: python

    # RECHERCHE : Minimum
    # Attention une fonction pédéfinie min existe déjà sera remplacée.
    def min(tab) -> int:
        '''Retourne le minimum d'un tab.
        Données
            tab: list, tableau d'entiers
        Sorite
            mn : int, valeur minimale
        Exemples
        >>> min([0, 5, 8]) == 0
        True
        '''
        mn = tab[0]  # minimum provisoire
        for i in range(1, len(tab)):    # PARCOURS
            if tab[i] < mn:             # COMPARAISON
                mn = tab[i]
        return mn

    # Appel
    t = [1, 2, 2, 5, 2, 8]

    resultat = min(t)
    print('Le minimum est', resultat)
  
    
Maximum d'un tableau
""""""""""""""""""""
.. code-block:: python

    ## RECHERCHE : Maximum
    # Attention une fonction pédéfinie max existe déjà sera remplacée.
    def max(tab) -> int:
        '''Retourne le maximum d'un tableau.
        Données
        -------
            tab: list, tableau d'entiers
        Sorite
        ------
            mx : int, valeur maximale
        Exemples
        --------
        >>> max([0, 5, 8]) == 8
        True
        '''
        assert len(tab) > 0, 'Tableau vide'
        mx = tab[0]          # maximum provisoire
        for i in range(1, len(tab)):
            if tab[i] > mx:
                mx = tab[i]  # maximum provisoire
        return mx

    # Appel
    t = [1, 2, 2, 5, 2, 8]

    resultat = max(t)
    print('Le maximum est', resultat)
    
Opérations sur les tableaux
---------------------------
Somme des éléments
""""""""""""""""""

.. code-block:: python

    def somme(tab) -> float:
        taille = len(tab)
        som = 0.0
        for i in range(taille):
            som += tab[i]
        return som

    # Appel
    taille = 5
    A = [0] * taille
    saisie(A)
    print(somme(A))

Somme de deux tableaux
""""""""""""""""""""""
.. code-block:: python

    def sommeTab(A, B) -> list:
        taille = len(A)
        assert len(B) == taille, '/?\ Dimensions incompatibles'
        som = [0.0] * taille  # création de tableau résultat
        for i in range(taille):
            som[i] = A[i] + B[i]
        return som

    # Appel
    taille = 5
    A = [0] * taille
    B = [0] * taille
    saisie(A)
    saisie(B)
    affichage(sommeTab(A, B))

Permutation
"""""""""""

.. code-block:: python

    def premutation(A, i, j):
        taille = len(A)
        assert 0 <= i <= j < taille, '/?\ Indices invalides'
        A[i], A[j] = A[j], A[i] # Affectation en série

Permutation circulaire
""""""""""""""""""""""
.. code-block:: python

    def premutationCirculaire(A, i_d, i_f):
        taille = len(A)
        assert 0 <= i_d < i_f < taille, '/?\ Indices invalides'
        temp = A[i_d]  # On sauvegarde valeur qui sera remplacée
        for i in range(i_d, i_f+1):
            A[i] = A[i+1]
        A[i_f] = temp  # On récupère la valeur sauvegardée

Permutation successive
""""""""""""""""""""""
.. code-block:: python

    def premutationSuccessive(A, i_d, i_f):
        taille = len(A)
        assert 0 <= i_d < i_f < taille, '/?\ Indices invalides'
        for i in range(i_d, i_f):
            A[i], A[i+1] = A[i+1], A[i]
            # premutation(A, i, i+1)        # solution possible

Inverse
"""""""

.. code-block:: python

    # premutation symétrique
    def inverser(A):
        taille = len(A)
        assert type(A) == list, '/?\ Ce n\'est pas un tableau'
        i_f = taille - 1
        for i in range(taille//2):  # premuter les deux moitiers
            i_c = i_f - i  # On peut utiliser ~i
            A[i], A[i_c] = A[i_c], A[i]
            # premutation(A, i, i_c)        # solution possible
