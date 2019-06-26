

def charger(fichier) -> str:
    '''
    '''
    with open(fichier, encoding='utf-8') as ms:
        texte = ms.read()
        return texte

traiter(texte)

def enregistrer(texte, fichier):
    with open(fichier, mode='w', encoding='utf-8') as fs:
        fs.write(texte)