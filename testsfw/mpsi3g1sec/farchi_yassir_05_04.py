def rle(texte):
    resultat = ''
    cpt = 0
    for i in range(len(texte)):
        cpt += 1
        if i == len(texte) - 1:
            if cpt == 1:
                cpt = 0
                resultat += texte[i]
            else:
                resultat += str(cpt) + texte[i]
                cpt = 0
        elif texte[i] != texte[i+1]:
            if cpt == 1:
                cpt = 0
                resultat += texte[i]
            else:
                resultat += str(cpt) + texte[i]
                cpt = 0
    return resultat
##
def decompression_rle_rle(donnee):
    cpt = 0 ; resultat = '' ; nbr =''
    for carac in donnee:
        try:
            cpt += int(carac)
            nbr += carac
        except:
            if nbr == '':
                resultat += carac
            else:
                resultat += carac*int(nbr)
                nbr = ''
    return resultat
##
def compresser_fichier(fichier, destination):
    with open(fichier, "r" , encoding="utf8") as file2comp:
        texte = rle(file2comp)
    with open(destination, "w" , encoding="utf8") as dest:
        dest = texte.write()
##
def decompresser_fichier(fichier,destination):
    with open(fichier, "r" , encoding="utf8") as file2comp:
        texte = decompression_rle(file2comp)
    with open(destination, "w" , encoding="utf8") as dest:
        dest = texte.write()
    
    
    
    
    
    
    
    
    
    
    
                