'''BADDOU FATIMA-ZOHRA
   MPSI3
   GROUPE1
'''
### rechercher les lignes ou il y a les mots qu'on veut 
def recherche(nom_du_fichier,mot_a_chercher)-> list:
	with open(fichier,mode='r',encoding='utf_8') as filetoread: #ouvrir le fichier et lire le contenu
		texte = filetoread.read
		liste = []
		for line in texte:
			if mot_a_chercher in line.split(): #chercher le mot dans les ligne
				liste = liste + line # créer les listes des lignes
				return liste

###insertion
def inserer(tab,element)->list:
    taille = len(tab)
    if element == 1 and tab[element] < tab[element + 1]: # si on veut l'ordre croissant
        tab[element],tab[element + 1] = tab[element + 1],tab[element]
    else :
        inserer(tab,element)

def inserer(tab,element)->list:
    taille = len(tab)
    if element == 1 and tab[element + 1] < tab[element]: # si on veut l'ordre decroissant
           tab[element + 1],tab[element] = tab[element],tab[element + 1]
    else :
        inserer(tab,element)

        
    
        
        
