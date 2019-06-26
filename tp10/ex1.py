
MAX_PILE = -1
# piles
def creer_pile():
    return [] # list()
    
# piles & files
def taille(tda):
    return len(tda)

def est_vide(tda):
    return len(tda) == 0

# piles
def est_pleine(pile):
    return MAX_PILE == taille(pile)

def empiler(pile, valeur):
    assert not est_pleine(pile)
    pile.append(valeur)
    
def sommet(pile):
    return pile[-1]
    
def depiler(pile):
    assert not est_vide(pile), 'Pile vide'
    return pile.pop()
    

