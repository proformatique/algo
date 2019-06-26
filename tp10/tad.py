"""TP11. File avec structure recursive circulaire."""


class BiNoeud:
    '''Structure recursive.'''
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
    '''File avec liste doublement chainee.

    >>> f = File(2)
    >>> f.enfiler(1)
    >>> f.enfiler(2)
    >>> f.defiler()
    1
    >>> f.defiler()
    2
    >>> f.defiler()
    Traceback (most recent call last):
    ...
    AssertionError: La file est vide!
    >>> f.tete()
    Traceback (most recent call last):
    ...
    AssertionError: La file est vide!
    '''
    def __init__(self, m=-1):
        """Cree des files de taille maximale m, -1 illimite."""

        self.file = None
        self.nbr = 0
        self.max = m

    def enfiler(self, elm):
        """Empile un element"""
        assert not self.est_pleine(), 'La file est pleine!'
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
        assert not self.est_vide(), 'La file est vide!'
        return self.file.get_valeur()

    def est_vide(self)-> bool:
        """Retourne True si la file est vide."""
        return self.nbr == 0

class Noeud:
    '''Structure récursive.'''
    def __init__(self, n=None, p=None):
        self.__valeur = n
        self.__precedent = p

    def get_valeur(self):
        return self.__valeur

    def get_precedent(self):
        return self.__precedent

    def set_valeur(self, valeur):
        self.__valeur = valeur


    def set_precedent(self, precedent):
        self.__precedent = precedent


class Pile:
    '''Pile en utilisant une liste chaînée.'''

    def __init__(self):
        self.pile = None
        self.nbr  = 0
        
    
    def empiler(self, elm):
        element = Noeud(elm, self.pile)
        self.pile = element
        self.nbr += 1
    
    def depiler(self):
        assert self.nbr > 0, 'Pile vide'
        element = self.pile.get_valeur()
        self.pile = self.pile.get_precedent()
        self.nbr -= 1
        return element
    
    def taille(self):
        return self.nbr
    
    def est_vide(self):
        return self.nbr == 0
    
    def sommet(self):
        assert self.nbr > 0, 'Pile vide'
        return self.pile.get_valeur()


if __name__ == '__main__':
    import doctest as dt
    dt.testmod(optionflags=dt.IGNORE_EXCEPTION_DETAIL, verbose=True)
