# directory tree
"""
./
|-- dir1/
|   |-- a/
|   |
|   |-- b/
|   `-- c/
|
`-- dir2/
"""

a = ['a', ['fichier1.txt'], ['fichier2.txt']]
b = ['b', ['fichier3.txt',]]
c = ['c', ['fichier4.txt',]]
dir1 = ['dir1', a, b, c]
a = ['a', ['fichier5.txt'], ['fichier6.txt',]]
b = ['b', ['fichier7.txt'], ['fichier8.txt',]]
c = ['c', ['fichier9.txt'], ['fichier10.txt',]]

dir2 = ['dir2', a, b, c]
courant = ['.', dir1, dir2]

def feuille(debut, fin):
    if fin > debut:
        feuille1 = [debut, debut+1, feuille(debut+2, fin-2), fin-1, fin]
    else:
        feuille1 = None
    return feuille1

cahier = feuille(1,16)

def printTree(dossiers, prefix=''):
    for fichier in dossiers:
        if type(fichier) == list:
            printTree(fichier, prefix+'   ')
        else:
            print(prefix + fichier)
printTree(courant)



'''
<<<<<<<<<
A
'''
class Noeud:
    '''Structure récursive.
      +=========+            
    _\| NOEUDN  |      
   / /|=========|   
   \__|precedent|
      |¨¨¨¨¨¨¨¨¨|
      |Valeur   |
      +=========+            
    '''
    def __init__(self, n=None, p=None):
        self.valeur = n
        self.precedent = p

class Pile:
    '''File doublement chaîné
            +=========+             +=========+            +=========+ 
            | NOEUDN-1|/_____       | NOEUDN  |/____       | NOEUDN+1|
            |=========|\      \     |=========|\     \     |=========|
    None <--|precedent|        \____|precedent|       \____|precedent|
            |¨¨¨¨¨¨¨¨¨|             |¨¨¨¨¨¨¨¨¨|            |¨¨¨¨¨¨¨¨¨|
            |valeur   |             |valeur   |            |valeur   |
            +=========+             +=========+            +=========+
                                                           (sommet/pile)
    '''
    def __init__(self):
        self.pile = None
        self.nbr  = 0
        
    
    def empiler(self, elm):
        element = Noeud(elm, self.pile)
        self.pile = element
        self.nbr += 1
    
    def depiler(self):
        assert self.nbr > 0, 'Pile vide'
        element = self.pile.valeur
        self.pile = self.pile.precedent
        self.nbr -= 1
        return element
    
    def taille(self):
        return self.nbr
    
    def est_vide(self):
        return self.nbr == 0
        
    
class File:
    def __init__(self):
        self.ecriture = Pile()
        self.lecture = Pile()
    
    def empiler(self, elt):
        while not self.lecture.est_vide():
            self.ecriture.empiler(self.lecture.depiler())
        self.ecriture.empiler(elt)
        
    def depiler(self):
        while not self.ecriture.est_vide():
            self.lecture.empiler(self.ecriture.depiler())
        return self.lecture.depiler()

class BiNoeud:
    '''Structure récursive.
      +=========+            
    _\| NOEUDN  |<-----     
   / /|=========|     :   
   \__|precedent|     :
      |¨¨¨¨¨¨¨¨¨|     : 
      |suivant  |------
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
              (tête)                                          (file) 
    '''
    def __init__(self, m=-1):
        self.file = None
        self.nbr = 0
        self.max = m
    
    def empiler(self, elm):
        assert not self.est_pleine(), 'La file est pleine!'
        element = BiNoeud(elm, p=self.file)
        if self.est_vide():
            self.file = element
            self.tete = self.file
        else:
            self.file.suivant = element
            self.file = element
        self.nbr += 1
    
    def est_pleine(self):
        return self.taille() == self.max
    
    def depiler(self):
        assert not self.est_vide(), 'Pile vide'
        element = self.tete.valeur
        self.tete = self.tete.suivant
        # self.tete.precedent = None
        self.nbr -= 1
        return element
    
    def taille(self):
        return self.nbr
    
    def est_vide(self):
        return self.nbr == 0

f = File()
f.empiler(0)
f.empiler(1)
f.empiler(2)
        
def tab(*dim):
    data = 0
    if len(dim) > 0:
        data = [[tab(*dim[1:])] for _ in range(dim[0])]
    return data

def print_nd(tab):
    print()
    for elt in tab:
        if type(elt) == list:
            print_nd(elt)
        else:
            print(elt, end='')
par = ')}]'
co = {'(':')','[':']','{':'}'}

def est_fermante(car):
    return car in par

def est_ouvrante(car):
    return car in co

def corr(car):
    return co[car]

    
def eval_expr(expr, par=[]):
    '''((()'''
    if expr == '':
        print(par,545454)
        res = par == []
    else:
        for i, car in enumerate(expr):
            if est_fermante(car):
                if len(par) == 0:
                    return False
                else:
                    parf = par.pop()
                    return parf == car
            elif est_ouvrante(car):
                print('ov', car, par)
                return eval_expr(expr[i+1:], par+[corr(car)])
"""
A = Noeud('A')
for a in 'BCDEFGHIJKLMNOPQRST':
    A = Noeud(a, A)

while A.precedent is not None:
    print(A.valeur)
    A = A.precedent
"""