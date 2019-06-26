''' 
Nom : El Bouzid
Prenom : Imane
Groupe : 1
Classe : MPSI 3
'''
def rle(texte) :
    copie = ''
    cpt = 1
    i = 0
    l = len(texte)
    if l == 0 :
        return copie
    if l == 1 :
        return texte
    while i < l - 1 :
        while i < l - 1 and texte[i] == texte[i+1] :
            cpt = cpt + 1
            i = i + 1
        if cpt == 1 :
            copie = copie + texte[i]
        else :
            copie = copie + str(cpt) + texte[i]
        i = i + 1
        cpt = 1
    return copie

def decompression_rle(texte) :
    nombres = '123456789'
    l = len(texte)
    copie = ''
    i = 0
    cpt = '0'
    if l == 0 or l == 1 :
        return texte
    while i < l :
        while texte[i] in nombres :
            cpt = cpt + texte[i]
            i = i + 1
        if cpt == '0' :
            copie = copie + texte[i]
        else :
            copie = copie + (int(cpt)*texte[i])
        cpt = '0'
        i = i + 1
    return copie

def compresser_fichier(fichier, destination) :
    with open(fichier, mode = 'r', encoding = 'utf-8') as ms :
        texte = ms.read()
    contenu = rle(texte)
    with open(destination, mode = 'w', encoding = 'utf-8') as copie :
        copie.write(contenu)

def decompresser_fichier(fichier, destination) :
    with open(fichier, mode = 'r', encoding = 'utf-8') as ms :
        texte = ms.read()
    contenu = decompression_rle(texte)
    with open(destination, mode = 'w', encoding = 'utf-8') as copie :
        copie.write(contenu)


    
    
    
    
    