def palyndrome(texte):
    if len(texte) < 2:
        pal = True
    else:
        premier = texte[0]
        dernier = texte[-1]
        texte = texte[1:-2]
        pal = premier == dernier and palyndrome(texte)
    return pal


def somme(liste: list):
    if len(liste) == 0:
        som = 0
    else:
        som = liste[0] + somme(liste[1:])
    return som


import recmodule as rec
rec.tree('.')
rec.os
print(rec.path)

with open('data.txt', 'rt') as dt:
    print(dt.read())


with open('nwaji.png', 'rb') as dt:
    print(dt.read(1))
