class date:
    def __init__(self, j, m, a):
        assert self.__estvalide(j, m, a)
        self.jour = j
        self.mois = m
        self.annee = a
    
    def __estvalide(j, m, a):
        pass
        