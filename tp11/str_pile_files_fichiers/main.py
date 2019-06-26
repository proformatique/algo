def compter_caracteres_successifs(texte, j):
    """Compte le nombre d'occurences successives du caractere j."""
    i = 0
    caractere = texte[j]
    while caractere == texte[j + i]:
        i += 1
        if j + i >= len(texte):
            break
    return caractere, i
    
def rle(texte):
    """Run length Encoding."""
    assert type(texte) == str, 'Il faut passer un texte'
    assert len(texte) > 1, 'La chaine est trop petite'
    # initialisation
    j = 0
    code = [] # '' 
    while True:
        caractere, nombre = compter_caracteres_successifs(texte, j)
        # code += caractere + str(nombre)
        code += [caractere, nombre]
        j += nombre
        if j >= len(texte):
            break
    return code

def enregistrer(coderle):
    """Premet d'enregistrer le code rle."""
    with open('code.rle', 'wt', 'utf-8') as fichierlogique:
        fichierlogique.write('\n'.join(map(str, coderle)))

def charger(fichier):
    """Permet de charger un fichier."""
    try:
        with open(fichier, 'rt', 'utf-8') as fichierlogique:
            texte = fichierlogique.read()
    except FileNotFoundError as msg:
        texte = ''
        print(msg)
    else:
        texte = texte.strip()
    return texte        
        