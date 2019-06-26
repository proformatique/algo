def rechercher(nom_du_fichier:str, mot_a_chercher:str)->list:
    '''
    Parcoure les lignes d'un fichier et retourne une liste des numéros de lingnes contenant un mot
    >>> rechercher('Tesla.txt','voitures')
    [1,6]
    '''
    L = []
    with open(nom_du_fichier, mode='r', encoding='utf_8') as txt:
        texte = txt.read()
    T = texte.split('\n')
    for i in range(len(T)):
        if mot_a_chercher in T[i]:
            L =+ [i+1]
    return L

if __name__ == "__main__":
    import doctest
    doctest.testmod()
##
def inserer(tableau:list, element:int)->list:
    '''
    Permet d'insérer un élement dans un fichier de manière à obtenir un tableau trié
    >>>inserer([1,2,4],3)
    [1,2,3,4]
    '''
    L=[]
    l = len(tableau)
    if len(tableau)==1:
        if tableau[0]<element:
            return tableau+[elemnt]
        else:
            return [element]+tableau
    else:
        if element in range(len(tableau)//2):
            L=inserer(tableau[0:int(l/2)], element)
        else:
            L = inserer(tableau[int(l/2):l], element)
        return L
if __name__ == "__main__":
    import doctest
    doctest.testmod()       
            
            
        