# -*- coding: utf-8 -*-
'''Tp10 : Piles et files.
##############
Objectifs :
-----------
    #. Manipulation des files.
    #. Manipulation des Piles.
'''

__author__ = 'A. MHAMEDI'
__version__ = '0.1'


def premier_file(file: object) -> object:
    '''Retourne le premier element d'une file (FIFO).

    Parameters
    ----------
    file : File
        une file initialisée.
    Returns
    -------
    premier : object
        premier élément de la file.
    See Also
    --------
    File.tete()
    Notes
    -----
    on peut créer une version avec une file de type list ou Queue.
    '''
    premier = file.defiler()  # FIFO
    return premier


if __name__ == '__main__':
    import doctest as dt
    dt.testmod()

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
