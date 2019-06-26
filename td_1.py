def division(x, y) -> float: # Données
    # y != 0                 # Traitement
    div = x / y # identificateurs page 2 cadre 3
    return div               # Résultat







# definitions 
def estSSA(x, y) -> bool:
    cmp = x > y
    return cmp

def non(x) -> bool:
    res = x == False # comment?
    return res
    
    
# appel aux fonctions    
div = division(15, 20)
print('division(15, 20) = ', div)
cmp = estSSA(16, 5)
print('estSSA(16, 5) = ', cmp)
print('non(0 == 0) = ', non(0 == 0))



