# variables globales
#       01234567890123456789012345
alph = 'abcdefghijklmnopqrstuvwxyz'
code = 'klmnopqrstuvwxyzabcdefghij'
c_k7 = 'defghijklmnopqrstuvwxyzabc'



def avautk(lettre : str) -> str:
    # variable locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    # code = 'klmnopqrstuvwxyzabcdefghij'
    return code[alph.index(lettre)]

def k7(lettre : str) -> str:
    '''
    >>> k7(
    '''
    return c_k7[alph.index(lettre)]
    
def indice(lettre:str)-> int:
    pass

def cesar(lettre:str, rot:int)-> str:
    i = alph.index(lettre)
    return alph[(i + rot) % len(alph)]

def codeavautk(texte):
    copie = ''
    # variable locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    for car in texte:
        if car in alph:
            car = avautk(car)
        copie += car
    return copie