# variables globales
A = 0, 0
B = 100, -100
C = 0, 10


#Structure de données
 
# solution = [A, B, C, D, E, B, D, E, C]
def mymap(p):
    '''Obj.
    Parameters
    ----------
       p : str
    Returns
    -------
       pc : tuple
    
    Examples
    --------
    >>> maymap('A')
    (100, -100) # A
    
    '''
    if p == 'A':
        pc = A # A variable globale
    elif p == 'B':
        pc = B
    elif p == 'C':
        pc = C
    elif p == 'D':
        pc = D
    elif p == 'E':
        pc = E
    return pc # variable locale

solution = "ABCDEBDEC"


# appel / test
for pointsuivant in solution:
    #turtle.goto(pointsuivant)
    print(mymap(pointsuivant))
