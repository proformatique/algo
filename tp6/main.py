from tp6.fichiers import charger
from tp6 import analyser, etendre 

def main():
    """Combinaison des fonctions."""
    path = 'appels.csv'
    dest = 'data.csv'
    contenutexte = charger(path)
    listedesappels = analyser(contenutexte)
    etendre(listedesappels)
    contenutexte = backtotext(listedesappels)
    enregistrer(contenutexte, dest)


if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
    main()
