class BiNoeud:
    '''Structure récursive.
      +=========+            
    _\| NOEUDN  |/____      
   / /|=========|\     \   
   \__|precedent|       |
      |¨¨¨¨¨¨¨¨¨|       |  
      |suivant  |______/
      +=========+            
    '''
    def __init__(self, v=None, p=None, s=None):
        self.valeur = v
        self.precedent = p
        self.suivant = s

class File:
    '''File doublement chaîné
            +=========+              +=========+            +=========+ 
            | NOEUDN-1|/_____  _____\| NOEUDN  |/____   ___\| NOEUDN+1|
            |=========|\     \/     /|=========|\     \/   /|=========|
    None <--|precedent|      /\______|precedent|      /\____|precedent|
            |¨¨¨¨¨¨¨¨¨|     /        |¨¨¨¨¨¨¨¨¨|     /      |¨¨¨¨¨¨¨¨¨|
            |suivant  |____/         |suivant  |____/       |suivant  |--> None
            |¨¨¨¨¨¨¨¨¨|              |¨¨¨¨¨¨¨¨¨|            |¨¨¨¨¨¨¨¨¨|
            |valeur   |              |valeur   |            |valeur   |
            +=========+              +=========+            +=========+    
              (tête)
                                                            (file) 
    >>> f = File(5)
    >>> f.empiler(1)
    >>> f.empiler(2)
    >>> f.empiler(3)
    >>> f.empiler(4)
    >>> f.empiler(5)
    >>> f.depiler()
    1
    >>> f.depiler()
    2
    >>> f.depiler()
    3
    >>> f.depiler()
    4
    >>> f.depiler()
    5
    >>> f.depiler()
    Traceback (most recent call last):
    ...
    AssertionError: La file est vide/!\    
    >>> f.tete()
    Traceback (most recent call last):
    ...
    AssertionError: La file est vide/!\
    '''
    def __init__(self, m=-1):
        self.file = None
        self.nbr = 0
        self.max = m
    
    def empiler(self, elm):
        assert not self.est_pleine(), 'La file est pleine/!\\'
        element = BiNoeud(elm)
        if self.est_vide():
            self.file = element
            self.file.precedent = element
            self.file.suivant = element
        else:
            self.file.precedent.suivant = element
            element.suivant = self.file
            element.precedent = self.file.precedent
            self.file.precedent = element           
        self.nbr += 1
    
    def est_pleine(self):
        return self.taille() == self.max
    
    def depiler(self):
        assert not self.est_vide(), 'Pile vide'
        element = self.file.valeur
        self.file.precedent.suivant = self.file.suivant
        self.file.suivant.precedent = self.file.precedent
        self.file = self.file.suivant
        self.nbr -= 1
        return element
    
    def taille(self):
        return self.nbr
    
    def tete(self):
        assert not self.est_vide(), 'La file est vide/!\\'
        return self.file.valeur
    
    def est_vide(self):
        return self.nbr == 0

if __name__ == '__main__':
    import doctest as dt
    dt.testmod(optionflags=dt.IGNORE_EXCEPTION_DETAIL,verbose=True)