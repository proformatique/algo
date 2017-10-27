TD5
====
Exercice 1
===========
1. Que donne le script suivant (sans utiliser la machine)
.. code-block:: python
	Tableau = [15.2, 14.75, 20.0] # on utilise une liste pour représenter un tableau
	taille = len(Tableau) # len : nombre d'éléments dans le tableau ici 3
	indice = 0            # indice du premier éléments Tableau[0] == 15.2
	while i < taille:
		print(indice, "Tableau[" + str(indice) + "]=", Tableau[indice])

2. Que fait la fonction str()?
3. Que fait l'opérateur +?
4. Corrigez le script
Exercice 2
==========
1. On a le script suivant

.. code-block:: python
	Notes = [15.2, 14.75, 20.0] # on utilise une liste pour représenter un tableau
	taille = len(Tableau) # len : nombre d'éléments dans le tableau ici 3
	indice = 0            # indice du premier éléments Tableau[0] == 15.2
	somme = 0             # somme des notes
	
	while indice < taille:
		#TODO: calculer la somme
		indice += 1
2. Complétez le script pour calculer la somme des notes.
3. Transformez le script en fonction qui calcule la moyenne.
4. Que pensez-vous du choix de la structure itérative while?
Exercice 3
==========
Créez une procédure qui permet de saisir un tableau


.. code-block:: python

	def saisie(tab):
		taille = len(tab) # len : nombre d'éléments dans le tableau
		lesindices = range(taille)  # intervalle des indices
		for indice in lesindices:
			#TODO: saisir les valeurs
			
Exercice 4
==========
Créez une procédure def afficher(tab) qui permet d'afficher les valeurs d'un tableau.


.. code-block:: python

	def afficher(tab):
		taille = len(tab) # len : nombre d'éléments dans le tableau ici 3
		lesindices = range(taille)  # intervalle des indices
		for indice in lesindices:
			#TODO: saisir les valeurs
Exercice 5
==========
1. Exécuter les programmes pour corriger les erreurs de syntaxe.
2. Utiliser l'outil http://pep8online.com pour vérifier le style du code-block proposé.
	
