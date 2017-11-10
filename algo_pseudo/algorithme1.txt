fonction comp1(N : entier, n : entier) : entier
variables
	c1 : entier
debut
    c1 ← 2 ** n - 1 - N
    retourne c1
fin

fonction valabs(x : entier) : entier
variables
	vabs : entier
début
	si x >= 0 alors
		vabs ← x
	sinon
		vabs ← -x
	finsi
	retourne vabs 
fin

procedure notationc1(N : entier, n : entier)
debut
	si N < 0 alors
		N ← comp1(N, n)
	finsi
	afficher(bin(N))	
fin	

procedure notationc1(N : entier, n : entier)
variables
	c1 : entier
debut
	si N < 0 alors
		c1 ← comp1(N, n)
	sinon
		c1 ← N
	finsi
	afficher(bin(c1))	
fin


procedure menu(): qui affiche

1 - Code binaire
2 - Notation C1
3 - Notation C2
4 - Notation biaisée
Que voulez vous faire?

procedure menu()
debut
	afficher("1 - Code binaire")
	afficher("2 - Notation C1")
	afficher("3 - Notation C2")
	afficher("4 - Notation biaisée")
	afficher("Que voulez vous faire?")
fin



algorithme principal pour demander 
à l'utilisateur un choix puis exécuter le traitement demandé

algorithme representation
constantes
	n ← 8
        k ← 127
variables
	N, choix : entier
debut
	menu()
	saisir(choix)
	afficher("Entrer le nombre à coder")
	saisir(N)
	si choix = 1 alors
		afficher(bin(N))
	sinonsi choix = 2 alors
		notationc1(N, n)
	sinonsi choix = 3 alors
		afficher("TODO") 
	sinonsi choix = 4 alors
		afficher("TODO")
	finsi
fin
        