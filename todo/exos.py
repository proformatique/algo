import TD5.td5_sol as td5
# print(td5.compter('m', 'mpsi'*3))
def comptertous(texte):
    #  01256
    # 'abcde'
    # [0,0,0,0,0]
    cpt = [0] * len(texte)
    for car in texte:
        i = td5.indice(car, texte)
        cpt[i] += 1
    return cpt