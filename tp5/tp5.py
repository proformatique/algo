# variables globales
#indice 00000000001111111111222222
#       01234567890123456789012345
alph = 'abcdefghijklmnopqrstuvwxyz'
code = 'klmnopqrstuvwxyzabcdefghij'
c_k7 = 'xyzabcdefghijklmnopqrstuvw'



def avautk(lettre : str) -> str:
    # variable locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    # code = 'klmnopqrstuvwxyzabcdefghij'
    return code[alph.index(lettre)]

def codeavautk(texte):
    copie = ''
    # variable locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    for car in texte:
        if car in alph:
            car = avautk(car)
        copie += car
    return copie

def k7(lettre: str) -> str:
    '''
    >>> k7()
    '''
    return c_k7[alph.index(lettre)]
    
def indice(lettre:str, texte:str)-> int:
    for i in range(len(texte)):
        if texte[i] == lettre:
            return i
    return -1

def cesar(lettre:str, rot:int)-> str:
    #i = alph.index(lettre)
    i = indice(lettre, alph)
    return alph[(i + rot) % len(alph)]
   
def codecesar(texte:str , rotation:int):
    copie = ''
    # variable locales
    # alph = 'abcdefghijklmnopqrstuvwxyz'
    for car in texte:
        if car in alph:
            car = cesar(car, rotation)
        copie += car
    return copie

if __name__ == '__main__':
    import td8
    with open('message.txt', encoding='utf-8') as ms:
        #rot = int(input('Entrer le code :'))
        texte = ms.read()
        td8.affichertout(texte)
        rot = 0
        print(alpha,compteurs, sep='\n')
        print(codecesar(texte, rot))
    
    
