^ Activité 2 : SRTUCTURES DE CONTROLE DE FLUX      
^               & SOUS-ALGORITHMES                  		   
fonction comp1(N : entier, n : entier) : entier
variables
	c1 : entier
debut
    c1 ← 2 ** n - 1 - N
    retourne c1
fin

^ ***************************************************************** ^
fonction valabs(N : entier) : entier
variables
	vabs : entier
début
	si N >= 0 alors
		vabs ← N
	sinon
		vabs ← -N
	finsi
	retourne vabs 
fin
^ ***************************************************************** ^
fonction valabs(N : entier) : entier
début
	si N < 0 alors
		N ← -N
	finsi
	retourne N 
fin
^ ***************************************************************** ^
procedure notationc1(N : entier, n : entier)
debut
	si N < 0 alors
		N ← valabs(N)
		N ← comp1(N, n)
	finsi
	afficher(bin(N))
fin	
^ ***************************************************************** ^
procedure notationc1(N : entier, n : entier)
variables
	c1, va : entier
debut
	si N < 0 alors
		va ← valabs(N)    {appel de fonction}
		c1 ← comp1(va, n) {appel de fonction}
	sinon
		c1 ← N
	finsi
	afficher(bin(c1))	
fin
^ ***************************************************************** ^
procedure menu()
debut
	afficher("1 - Code binaire")
	afficher("2 - Notation C1")
	afficher("3 - Notation C2")
	afficher("4 - Notation biaisée")
	afficher("5 - Quitter")
	afficher("Que voulez vous faire?")
fin
^ ***************************************************************** ^
^                          PROCEDURE PRINCIPALE                    ^
^ ***************************************************************** ^
algorithme representation
constantes
	n ← 8
    k ← 127
variables
	N, choix : entier
debut
	repeter
		menu()  			{appel de procédure}
		saisir(choix)
		afficher("Entrer le nombre à coder")
		saisir(N) 
		{On suppose que les données sont valides, sinon il faut 
		faire un contrôle de saisie }
		si choix = 1 alors
			afficher(bin(N)) 
		sinonsi choix = 2 alors
			notationc1(N, n) {appel de procédure}
		sinonsi choix = 3 alors
			afficher("TODO") 
		sinonsi choix = 4 alors
			afficher("TODO")
		finsi
	tantque choix <> 5
fin
        