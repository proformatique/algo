print(l-s)
class FilePriorite:
    def __init__(self, ordre='C'):
        self.__ordre = ordre

def insert(T, e, i=0, j=None):
    if len(T) == 0:
        return [e]
    else:
        if j is None:
            j = len(T)-1
        c = (i + j) // 2
        if e == T[c]:
            # e trouvé
            return T[:c] + [e] + T[c:]
        elif i == j:
            # e n'est pas dans le tableau 
            if e < T[0]:
                return [e] + T
            elif e > T[-1] :
                return T + [e]
            elif e < T[c]:
                return T[:c] + [e] + T[c:]
            else:
                return T[:c+1] + [e] + T[c+1:]
        elif e > T[c]:
            return insert(T, e, i+1, j)
        else:
            return insert(T, e, i, j-1)

T = []
for e in [5,56,62,4,8,5,9,6,3]:
    T = insert(T, e)
    
# TESTS
try:
    assert insert([1, 3, 5], 0) ==  [0, 1, 3, 5], "Ajout au début"
    assert insert([1, 3, 5], 2) ==  [1, 2, 3, 5], "Ajout avant"
    assert insert([1, 3, 5], 4) ==  [1, 3, 4, 5], "Ajout après"
    assert insert([1, 3, 5], 3) ==  [1, 3, 3, 5], "Ajout au milieu"
    assert insert([1, 3, 5], 6) ==  [1, 3, 5, 6], "Ajout au milieu"
    assert insert([], 6) ==  [6], "Ajout au milieu"

except AssertionError as probleme:
    print("Porblème au niveau de ", probleme)
else:
    print("tous les tests sont bien passés")


