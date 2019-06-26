paro = '[({'
parf = '])}'
    
def parouv(pf):
    return paro[parf.index(pf)]
    
def est_valide(expression):
    '''
    >>> est_valide('')
    True
    >>> est_valide(')(')
    False
    >>> est_valide('{c+([x-1]*2)}()[]')
    True
    >>> est_valide('((()()))')
    True
    >>> est_valide('(()()))')
    False
    '''
    pile = []
    for car in expression:
        if car in paro:
            pile += [car] # empiler ( [ ou {
        elif car in parf: # ) ] ou }
            if len(pile) == 0: # pile vide ?
                return False
            if pile[-1] == parouv(car): # sommet
                pile.pop() # dépiler 
            else:
                return False
    return len(pile) == 0
            








if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
    
    
    
    
    
    