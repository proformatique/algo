from tp11.tp11_.sda11 import File, Pile


pile2 = Pile()

operations = {
          '+': lambda a, b : a + b,
          '/': lambda a, b : a / b,
          '-': lambda a, b : a - b,
          '*': lambda a, b : a * b,
          '^': lambda a, b : a ** b,
          }
          
def calculer(a, b, op):
    assert op in operations, 'Opération non valide'
    if op == '/' and b == 0:
        raise ValueError('Opérande non valide')
    operation = operations[op] #  sélection de l'opération
    return operation(a, b) 
    
def evaluer(expression):
    pile1 = Pile()
    for car in expression:
        print(pile1, car ,sep='\nsuivant : ')
        if car in operations:
            b = float(pile1.depiler())
            a = float(pile1.depiler())
            resultat = calculer(a, b, car)
            print(pile1, resultat ,sep='\nsuivant : ')
            pile1.empiler(resultat)
        else:
            pile1.empiler(car)
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
