path = {
    'A' : ['A', 'E', 'B'],
    'B' : ['A', 'E', 'D', 'C'],
    'C' : ['B', 'E', 'D'],
    'D' : ['B', 'E', 'C'],
    'E' : ['B', 'A', 'D']
}
myp = []

def helper(myp, c, n):
    if n == 0:
        return myp
    else:
        pth = path[c]
        for dir in pth:
            # choose
            helper(myp, dir)
            # explore
            # un-choose

##
def binaire(chiffres, pre):
    if chiffres == 0:
        print(pre)
    else:
        binaire(chiffres-1, pre+"0")
        binaire(chiffres-1, pre+"1")

def decimal(chiffres, pre):
    if chiffres == 0:
        print(pre)
    else:
        for i in range(10):
            decimal(chiffres-1, pre+str(i))

##
def visited(path, seg):
    de, a = seg
    seg2 = a, de
    yes = seg in path or seg2 in path
    # print('visited', path, seg, seg2, yes)
    return yes
    
def traverser(path, seg):
    path.append(seg)

def notvisited(path, possib):
    nv = []
    for seg in possib:
        # print(seg)
        if not visited(path, seg):
            nv.append(seg)
    return nv
            
def possibilities(G, path, de=None):
    pos = []
    if not de or de not in G.keys():
        P = list(G.keys())
    else:
        P = G[de]
    # print(P)
    for a in P:
        seg = (de, a)
        # print(seg)
        pos.append(seg)
    pos = notvisited(path, pos)
    return pos
    
G = {'A' : ['B', 'E'],
     'B' : ['A', 'E', 'C', 'D'],
     'C' : ['B', 'E', 'D'],
     'D' : ['B', 'E', 'C'],
     'E' : ['A', 'B', 'C', 'D'],
    }
count = 0
countx = 0

def explore(G, path=[], choice=None):
    global count, countx
    decisions = possibilities(G, path, choice)
    # print(decisions)
    if not decisions:
        if len(path) == 8:
            for de, a in path:
                print(a, end='→')
            print('\n', '-' * 50)
            return True
        else:
            return False
    else:
        for seg in decisions:
            de, a = seg
            if de != None:
                traverser(path, seg)
            if explore(G, path, a):
                count += 1
            else:
                countx += 1
            if len(path) > 0:
                path.pop()
        return False
    
## parties d'un ensemble
ens = [1,2,3]

def partie(ens, part=[]):
    
    if 0 == len(ens):
        print(part)
        return True 
    else:
        o = ens[:i]
        for i in range(len(part)):
            p = part[:]
            e = o.pop()
            part.append(p)
            partie(ens, part)
            part.pop()

##
def anagram(ls, p=[], i):
    
    for c in ls:
        p.append(c)
        anagram(ls, p, c)
        p.pop()

def anagram(ch, c='', chosen=[]):
    if len(chosen) >= len(ch):
        print(c)
    else:
        for i in range(len(ch)):
            if i not in chosen:
                chosen.append(i)
                anagram(ch , c+ch[i], chosen)
                chosen.pop()

def filebrowser(file, d=''):
    for f in file:
        if type(f) != list:
            print(d,f)
        else:
            filebrowser(f, d+'\t')

##
def parties(liste, chosen=[], choice=''):
    if len(liste) == 0:
        print(chosen)
    else:
        for c in liste:
            d = liste.pop()
            chosen.append(c)
            parties(liste, chosen)
            chosen.pop()
            parties(liste, chosen)
            liste.append(d)
            