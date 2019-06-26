from math import sqrt

class Point:
    __compteur = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.plus1()
        
    def plus1():
        Point.__compteur += 1
        
    def card():
        return Point.__compteur
    
    def __str__(self):
        return "({}, {})".format(self.__x, self.__y)
    
    def __repr__(self):
        return self.__str__()
        
    # getters
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    # setters
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y
    
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
print('Nombre de points est de ', Point.card())