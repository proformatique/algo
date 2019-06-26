class Point:
    compteur = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y
        Point.compteur += 1
    
    def card():
        return Point.compteur
    
    def __str__(self):
        return "({}, {})".format(self._x, self._y)
    
    def __repr__(self):
        return self.__str__()
        
    # getters
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    # setters
    def setX(self, x):
        
        self._x = x
    
    def setY(self, y):
        self._y = y
    
    def dist(self, p):
        dst = sqrt((p.getX() - self.getX()) ** 2 
           + (p.getY() - self.getY()) ** 2)
        return dst
        
        
#

A = Point(0, 0)
B = Point(1, 1)
C = Point(0, 10)
D = Point(10, 1)

#print(A.getX(), A.getY())
print(A, B, C, D)
print('dist: A-->B ', A.dist(B))