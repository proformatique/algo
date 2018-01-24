alph = 'az'
def f(texte):
    cpt = {}
    for car in texte:
        cpt[car] = cpt.get(car, 0) + 1
    return cpt


def f(texte):
    cpts={}
    for car in texte:
        if car in cpts:
            cpts[car] += 1
        else:
            cpts[car] = 1
    return cpts




def maxd(d:dict):
    m = 0
    for k in d:
        if d[k] > m and k in alph:
            m = d[k]  
            km = k
    return km
    




#with open('ficdest.txt', mode='w', encoding='utf-8') as df:
#    df.write(texte)