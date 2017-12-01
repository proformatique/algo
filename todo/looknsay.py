
def ls(N):
    n = 1
    cpt = [0] * 10
    chiffres = []
    for _ in range(N):
        # decomposition et comptage
        cpt = [0] * 10
        chiffres = []
        while True:
            c = n % 10
            cpt[c] += 1
            if c not in chiffres:
                chiffres.insert(0, c)
            n //= 10
            if n == 0:
                break
        cf = []
        for a in chiffres[::-1]:
            cf.insert(0 ,a)
            cf.insert(0, cpt[a])
        chiffres = cf
        # composition
        for i in range(len(chiffres)):
            p = len(chiffres) - 1 - i
            n += chiffres[i] * 10 ** p       
        print(n)
#####################
n = 1
chiffres = []
for _ in range(8):
# decomposition et comptage
    chiffres = []
    print(n)
    while True:
        c = n % 10
        cpt = 0
        while n % 10 == c:
            cpt += 1
            n //= 10
            if n == 0:
                break
        chiffres.insert(0, c)
        chiffres.insert(0, cpt)
        if n == 0:
            break
    
    # composition
    for i in range(len(chiffres)):
        p = len(chiffres) - 1 - i
        n += chiffres[i] * 10 ** p 


    