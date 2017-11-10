# Activité 3 : SRTUCTURES DE CONTROLE DE FLUX      
#               & SOUS-ALGORITHMES                  		   

fonction produit(A: entier, B : entier): entier
variables 
    prd : entier ← 0        {résultat initialisé à 0}
	cpt : entier ← 0        {compteur}
debut
	tantque cpt < B faire   {attention à ne pas ← avoir une boucle infinie}
		prd ← prd + A
		cpt ← cpt + 1 		{compter les opérations}
	fintq
	retourne prd
fin



fonction puissance(A: entier, B : entier):entier
variables 
    res : entier ← 1        {résultat}
	cpt : entier ← 0        {compteur}
debut
	tantque cpt < B  faire   {attention à ne pas ← avoir une boucle infinie}
		res ← res * A
		cpt ← cpt + 1 		{compter les opérations}
	ftq
	retourne res
fin


# *************************    Boucle POUR *******************************^

fonction produit(A: entier, B : entier): entier
variables 
    prd : entier ← 0        {résultat}
	cpt : entier            {compteur}
debut
	pour cpt ← 0 jusqua B-1 pas ← 1 faire 
		{initialisation, incrémentation automatique}
		prd ← prd + A
	finpour
	retourne prd
fin

{appel}
x ← produit(3, 2)


fonction puissance(A: entier, B : entier):entier
variables 
    res : entier ← 1        {résultat}
	cpt : entier 		    {compteur}
debut
	pour cpt ← 0 jusqua B pas ← 1 faire   
		res ← res * A
	finpour
	retourne res
fin


fonction factorielle(N : entier): entier
variables
	res : entier ← 1
	k : entier
debut
	pour k ← 1 jusqua N faire
		res ← res * k
	finpour
	retourne res
fin

fonction somme(N : entier): entier
variables
	som : entier ← 0
	i : entier
debut
	pour i ← 0 jusqua N faire 
		som ← som + i
	finpour
	retourne som
fin

# TRANSCRIPTION EN PYTHON 

pour variable ← 0 jusqua 10 faire

finpour

for cpt in seq:
	bloc
	
# la séquence peut être :
# seq = range(start=0, stop, step=1)
# seq = "texte"

tantque condition faire
    bloc
fintq
	
while condition:
	bloc






