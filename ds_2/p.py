
def comptertout0(texte):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  
    cpt = [0] * len(alphabet)  # 0
    for car in texte:         # PARCOURS
        i = alphabet.index(car)  # COMPARAISON
        #i = indice(car, alphabet)        
        cpt[i] += 1
    return cpt

##
def comptertout1(texte):
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'  
    cpt = [0] * len(texte)  # 0
    for car in texte:         # PARCOURS
        i = texte.index(car)  # COMPARAISON
        #i = indice(car, texte)        
        cpt[i] += 1
    return cpt

##
def comptertout2(texte):
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = textesansd(texte)
    cpt = [0] * len(alphabet)    # 0
    for car in alphabet:         # PARCOURS
        i = alphabet.index(car)  # COMPARAISON
        #i = indice(car, alphabet)        
        cpt[i] += 1
    return cpt