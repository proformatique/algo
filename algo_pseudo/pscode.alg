# ****************     Structures itératives  *********************** #
## Syntaxe des boucles.
1 :

	tantque codition faire 
		bloc de code
	fintq

2 :

	pour cpt ← start jusqua stop pas ← step faire
		{start, stop: des nombres représentant les bornes de l'intervalle }
		bolc de code
	finpour
3 :

	repeter
		bolc de code
	tantque condition
4 :

	sortir
	continuer
$ En python.
1 :
while condition:
	bolc de code
2 :
for cpt in range(start, stop, step):
    {par défaut start = 0 step = 1}
	bolc de code

3 : 
while True :
    bolc de code
    if condition:
        break
4 :
break
continue
$ Sous-algorithmes.
1 :
fonction id(p1 : type, p2 : type) : type
constantes
variables   
debut
	retourne resultat                                  
fin
en python :
def id(p1, p2) -> type:
	bolc de code
	return retsultat
2 :
procedure id(p1 : type, p2 : type)
constantes
variables
debut
fin
en python :
def id(p1, p2):
	bolc de code
	
^**********************   Exercices d'application  ************************^
$ I - En utilisant la boucle tantque puis en utilisant pour.
1 . écrire une fonction produit(A: entier, B : entier): entier 
qui calcule A * B = A + A + ... + A } B fois
2 . écrire une fonction puissance(A: entier, B : entier): entier 
qui calcule A exposant B = A * A * ... * A } B fois
3 . écrire une fonction somme(N: entier): entier 
qui calcule som = 1 + 2 + 3 + ... + N
4 . écrire une fonction factorielle(N: entier): entier 
qui calcule N! = 1 * 2 * 3 * ... * N

$ II - Transcrire en python les 8 fonctions.
