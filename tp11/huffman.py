from queue import PriorityQueue


def double(d, f):
    if f - d > 4:
        return [d, d+1, double(d+2, f-2), f-1, f]
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
    p = double(d, f)
    r = recto(p)
    v = verso(p)
    return p, r, v


def frequences(texte):
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
    # print(prof * '...' + path , valeur)
    if len(valeur[1]) == 1:
        map[valeur[1]] = path
    if lc is not None:
        printtree(lc, path+'0', prof+1)
    if rc is not None:
        printtree(rc, path+'1', prof+1)


texte = """Return an iterator yielding those items of iterable for
which function(item) is true. If function is None, return the items \
 that are true."""


def zip(texte):
    cp = ''
    for car in texte:
        cp += map[car]
    return cp


# texte = """mi"""
freq = frequences(texte)
tr = tree(freq)
printtree(tr, '')
code = zip(texte)

livret = double(1, 16)
recto(livret)
