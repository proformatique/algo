Exercices
""""""""""
#. Définissez une fonction  qui retourne True si un tableau T est trié dans l'ordre croissant; sinon elle retourne False.

    .. code:: python

        def enOrdreCroissant() -> bool:

    .. autofunction:: tri.enOrdreCroissant


#. Définissez une fonction qui retourne True si un tableau T est trié dans l'ordre décroissant; sinon elle retourne False.

    .. code:: python

        def enOrdreDecroissant() -> bool:

    .. autofunction:: tri.enOrdreDecroissant

#. Combinez les codes des fonctions précédentes pour créer une fonction qui retourne True si un tableau T est trié (ordre croissant ou décroissant)

    .. code:: python

        def enordre(T) -> bool:

    .. autofunction:: tri.enOrdre

#. Définissez une fonction pour chercher une valeur v dans un tableau trié T.
    #. On regarde au milieu c du tableau [i..j]
    #. Si ce n'est pas la valeur recherchée:
        #. On regarde la prtie droite [c+1 .. j] si v est plus grande.
        #. On regarde dans la partie gauche [i..c-1] si v est plus petite.
    #. On répète la méthode jusqu'à ce qu'on trouve v ou bien i > j.

    .. code:: python

        def dichotomie(T) -> bool:

    .. autofunction:: tri.dichotomie

-------

#. Définissez une fonction qui retourne le nombre de chaque chiffre qui compose un entier n.

    .. code:: python

        def comptertous(n) -> bool:

    .. autofunction:: composition.comptertous

#. Définissez une fonction qui retourne True si un entier n est composé de chiffres distincts.

    .. python::

        def distincts(n) -> bool:

    .. autofunction:: decomposition.distincts

Problème I Le retour sur investissement
=======================================
Le retour sur investissement (RSI ou rentabilité du capital investi), parfois appelé rendement, taux de rendement, taux de profit ou encore ROI (terme anglais, Return On Investment), désigne un ratio financier qui mesure :

* le montant d'argent gagné ou perdu par rapport à la somme initialement investie dans un investissement.

En général, ce ratio est exprimé en pourcentage plutôt qu'en valeur décimale.

Rendement arithmétique
""""""""""""""""""""""
En termes mathématiques, on définit le "rendement arithmétique" comme suit :

:math:`{\displaystyle{RSI_{Arith}={\frac {V_{f}-V_{i}}{V_{i}}}={\frac {V_{f}}{V_{i}}}-1}}`

où

- :math:`{\displaystyle V_{i}}` est la valeur initiale de l'investissement et
- :math:`{\displaystyle V_{f}}` est la valeur finale de l'investissement

Ce rendement possède les caractéristiques suivantes :

* :math:`{\displaystyle RSI_{Arith}=+1.00=+100\%}` quand la valeur finale équivaut à deux fois la valeur initiale.
* :math:`{\displaystyle RSI_{Arith}>0}`  quand l'investissement est rentable
* :math:`{\displaystyle RSI_{Arith}<0}`  quand l'investissement est une perte
* :math:`{\displaystyle RSI_{Arith}=-1.00=-100\%}` quand on ne peut plus récupérer un investissement.

Question I.1 Définissez la fonction qui calcule :math:`RSI_{Arith}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: carremagique.rsiarith

Question I.2 Définissez la procédure qui affiche une explication du :math:`RSI_{Arith}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: carremagique.afficherrsi

--------

Problème II Carré magique
=========================

En mathématiques, un **carré magique** d’ordre n est composé de :math:`n^2` entiers strictement positifs, écrits sous la forme d’un tableau carré. Ces nombres sont disposés de sorte que leurs sommes sur chaque rangée, sur chaque colonne et sur chaque diagonale principale soient égales. On nomme alors **constante magique** (et parfois **densité**) la valeur de ces sommes.

Un carré magique normal est un cas particulier de carré magique, constitué de tous les nombres entiers de 1 à :math:`n^2`, où n est l’ordre du carré

Les premiers carrés magiques d'ordres 5 et 6 apparurent dans une encyclopédie publiée à Bagdad vers 983, l’Encyclopédie de la Fraternité de la pureté (Rasa'il Ikhwan al-Safa). Des carrés magiques plus simples étaient connus de plusieurs mathématiciens arabes antérieurs.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Magicsquareexample.svg/220px-Magicsquareexample.svg.png
    :height: 2cm
Un exemple de carré magique normal d’ordre 3 et de constante magique 15.

En respectant les entêtes des fonctions proposées
""""""""""""""""""""""""""""""""""""""""""""""""""
Question 1. Définissez la fonction qui calcule la somme de la rangée r du carré magique cm.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    def sommeRangee(cm, r) -> int:

.. autofunction:: carremagique.sommeRangee

Question 2. Définissez la fonction qui calcule la somme des éléments d'une colonne c.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    def sommeColonne(cm, c) -> int:

.. autofunction:: carremagique.sommeColonne


Question 3. Définissez la fonction qui calcule la somme des éléments de la diagonale d.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    def sommeDiagPrincipale(cm, d) -> int:

.. autofunction:: carremagique.sommeDiagPrincipale

--------------

Propriétés
""""""""""
Les sommes des deux carrés magiques des mêmes ordres donnent également des carrés magiques, mais le résultat n'est pas normal, c'est-à-dire que les nombres ne forment pas la suite 1, 2, 3... Également, la différence de deux carrés magiques du même ordre donne également un carré magique, mais qui n'est pas normal.

Question 4.a. Définissez la fonction qui retourne True si cm est magique, sinon False.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    def magique(cm) -> bool:

.. autofunction:: carremagique.magique

Question 4.b. Définissez la fonction qui retourne True si cm est normal, sinon False.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: python

    def magiqueNormal(cm) -> bool:

.. autofunction:: carremagique.magiqueNormal

Question 5. Définissez la fonction qui retourne un carrée magique somme de cm1 et cm2.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def sommeMagique(cm1, cm2, signe) -> list:

.. autofunction:: carremagique.sommeMagique

Le « produit » de deux carrés magiques crée un carré magique d'ordre supérieur aux deux multiplicandes. Ce produit s'effectue ainsi :

Soit les carrés magiques M et N :

#. Le carré final sera d'ordre M×N.
#. Diviser le damier final en N×N sous-damiers de M×M cases.
#. Dans le carré N, réduire de 1 la valeur de tous les nombres.
#. Multiplier ces valeurs réduites par M×M. Les résultats sont reportés dans les cases de chaque sous-damier correspondant du carré final.
#. Les cases du carré M sont additionnées N×N fois aux cases du damier final.


.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Magic_Squares_-_Multiplication_-_1.svg/330px-Magic_Squares_-_Multiplication_-_1.svg.png
   :height: 2cm

Soit à effectuer le « produit » de ces deux carrés magiques, un de 3×3 et l'autre de 4×4. Le carré magique final sera de 12×12.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Magic_Squares_-_Multiplication_-_2.svg/330px-Magic_Squares_-_Multiplication_-_2.svg.png
   :height: 6cm

Le carré magique de 3×3 est remplacé par le produit 3×3, alors que chaque nombre du carré 4×4 est diminué de 1.

Le damier final, de taille 12×12, est divisé en 4×4 sous-damiers, chacun ayant 3×3 cases. Chacune de ses cases s'obtient en multipliant 3×3 par l'une des cases du carré magique 4×4 « diminué ». Par exemple, 117 est le produit 3×3×13. Ce carré est magique, mais n'est pas normal. La prochaine étape va « corriger » cette « anomalie ».

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Magic_Squares_-_Multiplication_-_3.svg/330px-Magic_Squares_-_Multiplication_-_3.svg.png
   :height: 8cm

Après 4×4 additions du carré 3×3, le carré final est magique et normal.

Question 6. Définissez la fonction qui retourne une copie de cm après avoir diminué les valeurs de 1.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def diminuerCMagique(cm) -> list:

.. autofunction:: carremagique.diminuerCMagique

Question 7. Définissez la fonction qui retourne un tuple (r, c).
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def divisionMagique(i, j) -> tuple:

.. autofunction:: carremagique.divisionMagique

Question 8. Définissez la fonction qui retourne le produit de cm1 et cm2.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def produitMagique(cm1, cm2) -> list:

.. autofunction:: carremagique.produitMagique

Question 9. Définissez la fonction qui retourne une copie du damier final après adition de cmm à tous les sous-damiers.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    def additionMagique(cmf, cmm) -> list:

.. autofunction:: carremagique.additionMagique
