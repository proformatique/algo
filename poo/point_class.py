from math import sqrt

class Point:
    __x = None
    __y = None
    
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

A = Point()
B = Point()

A.setX(0)
A.setY(0)
print(A.getX(), A.getY())

B.setX(10)
B.setY(10)
print(B.getX(), B.getY())

print('dist: A--B ', A.dist(B))



