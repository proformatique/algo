def chercher(nom_du_fichier, nom_a_chercher):
    '''
    Cette fonction retourne un tableau qui comporte les indices des lignes qui comportent le nom a chercher '''
    
    T = []
    with open(nom_du_fichier, mode = 'r', encoding = 'utf-8') as fichier:
        contenu = fichier.readlines()
        for i,line in enumerate(contenu):
            if mot_a_chercher in line:
                T += [i + 1]
    return T
def inserer(tab,element):
    if len(tab) == 0:
        return tab+[element]
    if len(tab)== 1:
        if tab[0] < element :
            return tab +[element]
        else:
            return [element] + tab    

    else :
        T1 = tab[:len(tab)//2]
        T2 = tab[len(tab)//2:]
        if tab[len(tab)//2] > element :
            T1 = inserer(T1,element)
            return T1 + T2
        else :
            T2 = inserer(T2,element)
            return T1 + T2
'''
>>> inserer([2,5,8],3)
 [2, 3, 5, 8]
'''             

if __name__ == '__main__':
    import doctest as dt
    dt.testmod(verbose=True)
                    
        
                        
    