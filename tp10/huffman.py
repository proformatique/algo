from queue import PriorityQueue
from math import ceil

'''
Une définition récursive est une définition dans laquelle intervient ce que l’on
 veut définir. Un algorithme est dit récursif lorsqu’il est défini en fonction
 de lui-même.
'''

def double(d, f):
    if f - d > 4:
        return [d, d+1, double(d+2, f-2), f-1,f]
    else:
        return [d, d+1, f-1, f]

def recto(livret):
    if len(livret) > 4:
        pages = [livret[1]] + [livret[3]]
        pages += recto(livret[2])
    else:
        pages = [livret[1]] + [livret[2]]
    return pages

def verso(livret):
    if len(livret) > 4:
        pages = [livret[4]] + [livret[0]]
        pages += verso(livret[2])
    else:
        pages = [livret[3]] + [livret[0]]
    return pages
    
def print_livret(f):
    f = f + 4 - f % 4
    d = 1
    p = double(1, f)
    r = recto(p)
    v = verso(p)
    return p, r, v

def frequences(texte):
    '''Compte le nombre des occurences de chaque lettre de texte.'''
    cpts = {}
    for car in texte:
        cpts[car] = cpts.get(car, 0) + 1
    return cpts

myt = []

def tree(freq):
    fp = PriorityQueue()
    for k, v in freq.items():
        fp.put([(v, k)])
    while fp.qsize() > 1:
        e1 = fp.get()
        e2 = fp.get()
        v1, l1 = e1[0]
        v2, l2 = e2[0]
        v = v1 + v2
        lb = l1+l2
        Node = [(v, lb), e1, e2]
        fp.put(Node)
    return fp.get()
map = dict()
def printtree(t, path, prof=0):
    valeur = t[0]
    lc = t[1] if len(t) >= 2 else None
    rc = t[2] if len(t) >= 3 else None
    #print(prof * '...' + path , valeur)
    if len(valeur[1]) == 1:
        map[valeur[1]] = path
    if lc is not None: printtree(lc,path+'0', prof +1)
    if rc is not None: printtree(rc,path+'1', prof +1)

texte = """this is an example of a huffman tree"""

def zip(texte):
    cp = ''
    for car in texte:
        cp += map[car]
    return cp

def decode(tree, branche, code, i=0):
    if i < len(code):
        if branche is not None and len(branche) == 1:
            print(branche[0][1], end='')
            branche = tree
        else:
            bit = code[i]
            i += 1
            indice = int(bit) + 1
            if branche is None:
                branche = tree[indice]
            else:
                branche = branche[indice]
        decode(tree, branche, code, i)
        
'''with open('data.txt', encoding='utf-8') as f:
    texte = f.read()
    freq = frequences(texte)
    tr = tree(freq)
    printtree(tr, '')
    code = zip(texte)
    oct = ceil(len(code) / 8)
    dt = int(code[::-1], 2).to_bytes(oct, 'little')

with open('data.bnr', 'wb') as f2:
    f2.write(dt)
'''
#
from lolviz import treeviz


class Tree:
    def __init__(self, node):
        assert isinstance(node, (list, Tree))
        left, right = None, None
        if len(node) == 3:
            value, left, right = node
        elif len(node) == 2:
            value, left = node
        else:
            value = node[0]
        self.value = value
        self.left = left
        self.right = right
        
    
    def __str__(self):
        return str(self.value)+ '\n\t\t ' +str(self.right) + '\n\t\t '  + str(self.left)
        
root = Tree([(36, 'aehilomnprstuxf '),
 Tree([(16, 'aehilom'),
  Tree([(8, 'ae'), Tree([(4, 'a')]), Tree([(4, 'e')])]),
  Tree([(8, 'hilom'),
   Tree([(4, 'hi'), Tree([(2, 'h')]), Tree([(2, 'i')])]),
   Tree([(4, 'lom'), Tree([(2, 'lo'), Tree([(1, 'l')]), Tree([(1, 'o')])]), Tree([(2, 'm')])])])]),
 Tree([(20, 'nprstuxf '),
  Tree([(8, 'nprst'),
   Tree([(4, 'npr'), Tree([(2, 'n')]), Tree([(2, 'pr'), Tree([(1, 'p')]), Tree([(1, 'r')])])]),
   Tree([(4, 'st'), Tree([(2, 's')]), Tree([(2, 't')])])]),
  Tree([(12, 'uxf '),
   Tree([(5, 'uxf'), Tree([(2, 'ux'), Tree([(1, 'u')]), Tree([(1, 'x')])]), Tree([(3, 'f')])]),
   Tree([(7, ' ')])])])])

treeviz(root)
