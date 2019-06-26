"""
x  /x expr
      x != True
      x == False
v  f  f
f  v  v
"""
# Définitions

def non(x) -> bool:   # param : D
    neg = x != True   # Operat: T
    return neg        # Retour: R
    
# Test & appel
print('- test 1 =', non(True))
print('- test 2 =', non(False))

