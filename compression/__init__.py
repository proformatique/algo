import queue


def compter(texte):
    compteurs = {}
    for car in texte:
        compteurs[car] = compteurs.get(car, 0) + 1
    return compteurs



def bm(pq):
    if pq.qsize() > 1:
        elt1 = pq.get()
        elt2 = pq.get()
        s = elt1[0][0] + elt2[0][0]
        lbl =  elt1[0][1] + elt2[0][1]
        elt = [(s, lbl) , elt1, elt2]
        pq.put(elt)
        return bm(pq)
    return pq.get()
  

def code(tree, cd):
    if tree[2] is None and tree[1] is None:
        codes[tree[0][1]] = cd
    else:
        code(tree[1], cd + '0')
        code(tree[2], cd + '1')
        

c = compter("ab ab cab.")
pq = queue.PriorityQueue()
for k, v in c.items():
    elt = [(v , k), None, None]
    pq.put(elt)
    
q = bm(pq)
codes = {}
code(q, '')