def rle(texte):
    a = ''
    while len(texte)!=0:
        n = 1
        for i in range(len(texte)-1):
            if texte[i] == texte[i+1]:
                n += 1
            else: 
                break
        if n != 1:
            a += str(n)
        a += texte[0]
        texte = texte[n::]
    return a

def decompression_rle(texte):
    a = ''
    i = 0
    while i < len(texte):
        b = ''
        for j in range(i, len(texte)):
            if str.isdecimal(texte[j]):
                b += texte[j]
            else: 
                break
        if b != '':
            n = int(b)
        else :
            n = 1
        a += texte[j]*n
        i += j+1
    return a
            
def compresser_fichier(fichier, destination):
    with open("fichier", encoding = 'utf-8') as f:
        a = ''
        for ligne in f:
            a += rle(ligne) + '\n'
            with open("destination", "w", encoding = 'utf-8') as d:
                d.write(a)

def decompresser_fichier(fichier, destination):
    with open("fichier", encoding = 'utf-8') as f:
        a = ''
        for ligne in f:
            a += decompression_rle(ligne) + '\n'
            with open("destination", "w", encoding = 'utf-8') as d:
                d.write(a)