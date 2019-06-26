from sda11 import File, Pile
operations = {
          '+': lambda a, b : a + b,
          '/': lambda a, b : a / b,
          '-': lambda a, b : a - b,
          '*': lambda a, b : a * b,
          '^': lambda a, b : a ** b,
          }
          
def calculer(a, b, op):
    assert est_operateur(op), 'Opération non valide'
    if op == '/' and b == 0:
        raise ValueError('Opérande non valide')
    operation = operations[op] #  sélection de l'opération
    return operation(a, b) 

def est_operateur(op):
    return op in operations
    
def evaluer(expression):
    pile1 = Pile()
    for car in expression:
        print(pile1, car ,sep='  suivant : ')
        if est_operateur(car):
            b = pile1.depiler()
            a = pile1.depiler()
            resultat = calculer(a, b, car)
            print(pile1, resultat, sep='  suivant : ')
            pile1.empiler(resultat)
        else:
            pile1.empiler(int(car))
    return pile1.depiler()






def postfix(expression):
    pile1 = Pile()
    for car in expression:
        if car in operations:
            temp = pile1.depiler()
            pile1.empiler(car)
            pile1.empiler(temp)
        else:
            pile1.empiler(car)
    return pile1
