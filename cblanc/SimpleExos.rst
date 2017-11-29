# Carré magique
En mathématiques, un **carré magique** d’ordre n est composé de n\**2 entiers strictement positifs, écrits sous la forme d’un tableau carré. Ces nombres sont disposés de sorte que leurs sommes sur chaque rangée, sur chaque colonne et sur chaque diagonale principale soient égales. On nomme alors **constante magique** (et parfois **densité**) la valeur de ces sommes.

Un carré magique normal est un cas particulier de carré magique, constitué de tous les nombres entiers de 1 à n\**2, où n est l’ordre du carré

Les premiers carrés magiques d'ordres 5 et 6 apparurent dans une encyclopédie publiée à Bagdad vers 983, l’Encyclopédie de la Fraternité de la pureté (Rasa'il Ikhwan al-Safa). Des carrés magiques plus simples étaient connus de plusieurs mathématiciens arabes antérieurs.

![Carré magique normal](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Magicsquareexample.svg/220px-Magicsquareexample.svg.png)

__Un exemple de carré magique normal d’ordre 3 et de constante magique 15.__

.. codeblock::python

    #Question 1.
    def sommeRangee(cm, r) -> int:
        '''Retourne la somme de la rangée r du carré magique cm.
        Donnée
        ------
            cm : list, carré magique
            r : int, indice de la rangée
        Sortie
        ------
            sommeRg : int, somme de la rangée
        '''
        #ToDo: donner le code de la fonction
    
    #Question 2.    
    def sommeColonne(cm, c) -> int:
        '''Retourne la somme de la colonne c du carré magique cm.
        Donnée
        ------
            cm : list, carré magique
            c : int, indice de la colonne
        Sortie
        ------
            sommeCl : int, somme de la colone
        '''
        #ToDo: donner le code de la fonction
        
    #Question 3.
    def sommeDiagPrincipale(cm, d) -> int:
        '''Retourne la somme de la diagonale principale.
        Donnée
        ------
            cm : list, carré magique
            d : int, 1 pour la première diagonale et 2 pour la deuxième diagonale
        Sortie
        ------
            sommeDg : int, somme de la diagonale
        '''
        #ToDo: donner le code de la fonction
```

## Propriétés
Les sommes des deux carrés magiques des mêmes ordres donnent également des carrés magiques, mais le résultat n'est pas normal, c'est-à-dire que les nombres ne forment pas la suite 1, 2, 3... Également, la différence de deux carrés magiques du même ordre donne également un carré magique, mais qui n'est pas normal.

```python

    #Question 4.a
    def magique(cm) -> bool:
        '''Retourne True si cm est magique.
        Donnée
        ------
            cm : list, carré d'ordre N.
        Sortie
        ------
            magique : bool, True si cm est magique, sinon False.
        '''
        #ToDo: donner le code de la fonction

    #Question 4.b
    def magiqueNormal(cm) -> bool:
        '''Retourne True si cm est normal.
        Donnée
        ------
            cm : list, carré magique
        Sortie
        ------
            normal : bool, True si cm est normal, sinon False.
        '''
        #ToDo: donner le code de la fonction
    
    #Question 5.   
    def sommeMagic(cm1, cm2, signe) -> list:
        '''Retourne un carrée magique somme de cm1 et cm2.
        Données
        ------
            cm1 : list, carré magique.
            cm2 : list, carré magique.
            signe : str, signe '+' pour la somme '-' pour la soustraction
        Sortie
        ------
            sommeMg : list, somme ou soustraction terme à terme de cm1 et cm2.
        '''
        #ToDo: donner le code de la fonction
```

Le « produit » de deux carrés magiques crée un carré magique d'ordre supérieur aux deux multiplicandes. Ce produit s'effectue ainsi : 

Soit les carrés magiques M et N :
1. Le carré final sera d'ordre M×N.
1. Diviser le damier final en N×N sous-damiers de M×M cases.
1. Dans le carré N, réduire de 1 la valeur de tous les nombres.
1. Multiplier ces valeurs réduites par M×M. Les résultats sont reportés dans les cases de chaque sous-damier correspondant du carré final.
1. Les cases du carré M sont additionnées N×N fois aux cases du damier final.
   
![Produit magique 1](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Magic_Squares_-_Multiplication_-_1.svg/330px-Magic_Squares_-_Multiplication_-_1.svg.png)

    Soit à effectuer le « produit » de ces deux carrés magiques, un de 3×3 et l'autre de 4×4. Le carré magique final sera de 12×12.
![Produit magique 1](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Magic_Squares_-_Multiplication_-_2.svg/330px-Magic_Squares_-_Multiplication_-_2.svg.png)

    Le carré magique de 3×3 est remplacé par le produit 3×3, alors que chaque nombre du carré 4×4 est diminué de 1. Le damier final, de taille 12×12, est divisé en 4×4 sous-damiers, chacun ayant 3×3 cases. Chacune de ses cases s'obtient en multipliant 3×3 par l'une des cases du carré magique 4×4 « diminué ». Par exemple, 117 est le produit 3×3×13. Ce carré est magique, mais n'est pas normal. La prochaine étape va « corriger » cette « anomalie ».
    
![Produit magique 4](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Magic_Squares_-_Multiplication_-_3.svg/330px-Magic_Squares_-_Multiplication_-_3.svg.png)

    Après 4×4 additions du carré 3×3, le carré final est magique et normal.


```python

    #Question 6.
    def reduireCMagique(cm) -> list:
        '''Retourne une copie de cm après réduction.
        Données
        ------
            cm : list, carré magique d'ordre M.
        Sortie
        ------
            cm_1 : list, copie réduite de cm.
        '''
        #ToDo: Donner le code de la fonction
    
    #Question 7.
    def divisionMagique(i, j) -> tuple:
        '''Retourne un tuple r, c.
        Données
        ------
            i : int, ligne dans le carré final d'ordre M x N.
            j : int, colonne dans le carré final d'ordre M x N.
        Sortie
        ------
            r : int, premier indice du sous-carré d'ordre N dans le carré final.
            c : int, deuxième indice du sous-carré d'ordre N dans le carré final.
        '''
        #ToDo: Donner le code de la fonction
        
    #Question 8.
    def produitMagique(cm1, cm2) -> list:
        '''Retourne le produit de cm1 et cm2.
        Données
        ------
            cm1 : list, carré magique d'ordre M.
            cm2 : list, carré magique d'ordre N.
        Sortie
        ------
            produitMg : list, produit de cm1 et cm2.
        '''
        #ToDo: Donner le code de la fonction

    #Question 9.
    def additionMagique(cmf, cmm) -> list:
        '''Retourne une copie du damier final après adition de cmm à tous les sous-damiers.
        Données
        ------
            cmf : list, carré magique final d'ordre M x N.
            cmm : list, carré magique d'ordre M.
        Sortie
        ------
            cmfNormal : list, produit final normal.
        '''
        #ToDo: Donner le code de la fonction
```
# Problème
## Le retour sur investissement

Le retour sur investissement (RSI ou rentabilité du capital investi), parfois appelé rendement, taux de rendement, taux de profit ou encore ROI (terme anglais, Return On Investment), désigne un ratio financier qui mesure :

* le montant d'argent gagné ou perdu par rapport à la somme initialement investie dans un investissement.

En général, ce ratio est exprimé en pourcentage plutôt qu'en valeur décimale.

On désigne le gain ou la perte d'argent comme intérêt, profit / perte, gain/perte ou bien encore recette/perte. Pour se référer à l'argent investi, on emploie les termes d'actif, de capitaux, de somme principale ou de valeur d'acquisition de l'investissement.

## Rendement arithmétique

En termes mathématiques, on définit le "rendement arithmétique" comme suit :

.. math::

    {\displaystyle RSI_{Arith}={\frac {V_{f}-V_{i}}{V_{i}}}={\frac {V_{f}}{V_{i}}}-1} RSI_{{Arith}}={\frac  {V_{f}-V_{i}}{V_{i}}}={\frac  {V_{f}}{V_{i}}}-1

où
* ```math {\displaystyle V_{i}} ``` V_i est la valeur initiale de l'investissement et
* ```{\displaystyle V_{f}}``` V_f est la valeur finale de l'investissement

Ce rendement possède les caractéristiques suivantes :

* ``` math {\displaystyle RSI_{Arith}=+1.00=+100\%} RSI_{{Arith}}=+1.00=+100\% ```quand la valeur finale équivaut à deux fois la valeur initiale
* ```{\displaystyle RSI_{Arith}>0} RSI_{{Arith}}>0 ```quand l'investissement est rentable
* ```{\displaystyle RSI_{Arith}<0} RSI_{{Arith}}<0 ``` quand l'investissement est une perte
* ```{\displaystyle RSI_{Arith}=-1.00=-100\%} RSI_{{Arith}}=-1.00=-100\% ```quand on ne peut plus récupérer un investissement.
1. Exercice
Les tableaux peuvent contenir des données de différents types homogènes
- [ ] Vrai
- [ ] Faux

1. Exercice
