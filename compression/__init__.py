import queue


def compter(texte):
    compteurs = {}
    for car in texte:
        compteurs[car] = compteurs.get(car, 0) + 1
    return compteurs



def bm(pq):
    if len(pq.size()) > 1:
        elt1 = pq.get()
        elt2 = pq.get()
        s = elt1[0] + elt2[0]
        elt = [(s, elt1) ,elt2]
        
        return bm(file)
  
         
def code(tree, cd):
    print(tree, cd)
    if tree[2] is None:
        return tree[1], cd
    else:
        return code(tree[1], cd + '0')
        return code(tree[2], cd + '1')
        

c = compter("ab ab cab.")
pq = queue.PriorityQueue()
for k, v in c.items():
    elt = (v , k)
    pq.put(elt)
    
q = bm(file)
co = code(q, '')