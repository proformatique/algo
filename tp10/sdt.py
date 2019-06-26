"""TP11. File avec structure recursive circulaire."""


class BiNoeud:
    '''Structure recursive.
      +=========+
    __| NOEUDN  | ____
   |  |=========|     |
   |__|precedent|     |
      |---------|     |
      |suivant  |_____|
      +=========+
    '''
    def __init__(self, v=None, p=None, s=None):
        self.__valeur = v
        self.__precedent = p
        self.__suivant = s

    def set_precedent(self, precedent):
        """Retourne le precedent."""
        self.__precedent = precedent

    def set_suivant(self, suivant):
        """Retourne le suivant."""
        self.__suivant = suivant

    def set_valeur(self, valeur):
        """Retourne la valeur."""
        self.__valeur = valeur

    def get_precedent(self):
        """Retourne le precedent."""
        return self.__precedent

    def get_suivant(self):
        """Retourne le suivant."""
        return self.__suivant

    def get_valeur(self):
        """Retourne la valeur."""
        return self.__valeur


class File:
    '''File doublement chainee.

               +=========+          +=========+          +=========+
               | NOEUD_P |___    ___| NOEUD_N |___    ___| NOEUD_S |
               |=========|   |  |   |=========|   |  |   |=========|
    (NOEUD_S)<-|precedent|   |__|___|precedent|   |__|___|precedent|
               |---------|      |   |---------|      |   |---------|
               |suivant  |______|   |suivant  |______|   |suivant  |-->(NOEUD_P)
               |---------|          |---------|          |---------|
               |valeur   |          |valeur   |          |valeur   |
               +=========+          +=========+          +=========+
               (tête/file)                                    

    >>> f = File(5)
    >>> f.enfiler(1)
    >>> f.enfiler(2)
    >>> f.enfiler(3)
    >>> f.enfiler(4)
    >>> f.enfiler(5)
    >>> f.defiler()
    1
    >>> f.defiler()
    2
    >>> f.defiler()
    3
    >>> f.defiler()
    4
    >>> f.defiler()
    5
    >>> f.defiler()
    Traceback (most recent call last):
    ...
    AssertionError: La file est vide/!\
    >>> f.tete()
    Traceback (most recent call last):
    ...
    AssertionError: La file est vide/!\
    '''
    def __init__(self, m=-1):
        """Cree des files de taille maximale m, -1 illimite."""

        self.file = None
        self.nbr = 0
        self.max = m

    def enfiler(self, elm):
        """Empile un element"""
        assert not self.est_pleine(), 'La file est pleine/!\\'
        element = BiNoeud(elm)
        if self.est_vide():
            self.file = element
            self.file.set_precedent(element)
            self.file.set_suivant(element)
        else:
            self.file.get_precedent().set_suivant(element)
            element.set_suivant(self.file)
            element.set_precedent(self.file.get_precedent())
            self.file.set_precedent(element)
        self.nbr += 1

    def est_pleine(self):
        """Retourne True si la taille maximale est atteinte."""
        return self.taille() == self.max

    def defiler(self):
        """Retourne le premier element (FIFO)."""
        assert not self.est_vide(), 'Pile vide'
        element = self.file.get_valeur()
        self.file.get_precedent().set_suivant(self.file.get_suivant())
        self.file.get_suivant().set_precedent(self.file.get_precedent())
        self.file = self.file.get_suivant()
        self.nbr -= 1
        return element

    def taille(self)-> int:
        """Retourne La taille de la file."""
        return self.nbr

    def tete(self):
        """Retourne La tete de la file."""
        assert not self.est_vide(), 'La file est vide/!\\'
        return self.file.get_valeur()

    def est_vide(self)-> bool:
        """Retourne True si la file est vide."""
        return self.nbr == 0

if __name__ == '__main__':
    import doctest as dt
    dt.testmod(optionflags=dt.IGNORE_EXCEPTION_DETAIL, verbose=True)
