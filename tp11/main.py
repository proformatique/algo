"""TP10 & TP11.
Pour executer le module principal sous PyZo appuyez sur Ctrl+Shift+E
"""


def premier_file(file):
    return file.tete()


def premier_pile(pile):
    for i in range(pile.taille()):
        p = pile.depiler()
    return p


if __name__ == '__main__':
    # from tp11.sdtc import File
    from tp11.sdt import File
    # Instanciation
    file = File()
    # pile = Pile()
    # Initialisation
    for x in range(1, 20, 3):
        file.enfiler(x)
    # Utilisation
    print(premier_file(file))
