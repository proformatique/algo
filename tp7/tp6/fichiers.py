def charger(fichier: str) -> str:
    """Charge le fichier spécifié.

    Parameters
    ----------
    fichier :
        nom du fichier texte.

    Returns
    -------
    texte : contenu du fichier texte.
    """
    with open(fichier, encoding='utf-8') as file2read:
        texte = file2read.read()
        return texte.strip()


def enregistrer(texte: str, fichier: str):
    """Enregistre le texte dans le fichier spécifié.

    Parameters
    ----------
    texte :
        contenu du fichier à enregistrer.
    fichier :
        nom du fichier texte.

    """
    with open(fichier, mode='w', encoding='utf-8') as file2save:
        file2save.write(texte)

