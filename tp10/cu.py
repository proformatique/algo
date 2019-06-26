"""
Taille de l'alphabet
Le codage de Huffman

David Huffman a proposé en 1952 une méthode statistique qui permet d'attribuer
un mot de code binaire aux différents symboles à compresser (pixels ou caractères par exemple).
La longueur de chaque mot de code n'est pas identique pour tous les symboles: les symboles
les plus fréquents (qui apparaissent le plus souvent) sont codés avec de petits
mots de code, tandis que les symboles les plus rares reçoivent de plus longs codes binaires. On parle de codage à longueur variable (en anglais VLC pour variable code length)
préfixé pour désigner ce type de codage car aucun code n'est le préfixe d'un autre.
Ainsi, la suite finale de mots codés à longueurs variables sera en moyenne plus petite qu'avec un codage de taille constante.



Le codeur de Huffman crée un arbre ordonné à partir de tous
les symboles et de leur fréquence d'apparition. Les branches sont construites récursivement
en partant des symboles les moins fréquents.



La construction de l'arbre se fait en ordonnant dans un premier temps les symboles par fréquence d'apparition.
successivement les deux symboles de plus faible fréquence d'apparition sont retirés de la liste
et rattachés à un noeud dont le poids vaut la somme des fréquences des deux symboles. Le symbole
de plus faible poids est affecté à la branche 1, l'autre à la branche 0 et ainsi de suite en considérant
chaque noeud formé comme un nouveau symbole, jusqu'à obtenir un seul noeud parent appelé racine.
Le code de chaque chaque symbole correspond à la suite des codes le long du chemin allant de ce caractère
à la racine. Ainsi, plus le symbole est "profond" dans l'arbre, plus le mot de code sera long. 
"""
from queue import PriorityQueue
class Noeud:
    def __init__(self, valeur, code='', parent=None, gauche=None, droite=None):
        self.__valeur = valeur
        self.__code = code
        self.__parent = parent
        self.__gauche = gauche
        self.__droite = droite
    
    def get_poids(self):
        return self.__valeur[0]
    
    def __lt__(self, o):
        return self.get_poids() < o.get_poids() 
    
    def __le__(self, o):
        return self.get_poids() < o.get_poids() 
        
    def __str__(self):
        return self.get_code() + '' + str(self.get_valeur()) + '\n' + str(self.__gauche) + '\n' + str(self.__gauche)
    
    def __repr__(self):
        return self.__str__()
        
        
    def set_gauche(self, gauche):
        assert isinstance(gauche, Noeud), 'Doit prendre un noeud!'
        gauche.set_code('0')
        gauche.set_parent(self)
        self.__gauche = gauche
        
    def set_droite(self, droite):
        assert isinstance(droite, Noeud), 'Doit prendre un noeud!'
        droite.set_code('1')
        droite.set_parent(self)
        self.__droite = droite
    
    def set_parent(self, p):
        self.__parent = p
        
    def get_gauche(self):
        return self.__gauche
        
    def get_droite(self):
        return self.__droite
            
    def est_feuille(self):
        return not (self.__gauche or self.__droite)
    
    def get_parent(self):
        return self.__parent
    
    def get_valeur(self):
        return self.__valeur
    
    def get_code(self):
        parent = self.get_parent()
        code_pere = parent.get_code() if parent is not None else ''
        mon_code = self.__code
        return code_pere + mon_code
    
    def set_code(self, c):
        self.__code = c
    
#
def calculer_frequence(texte):
    frequences = {}
    for car in texte:
        frequences[car] = frequences.get(car, 0) + 1
    return frequences


def creer_arbre(frequences):
    file_priorite = PriorityQueue()
    for valeur in frequences.items():
        file_priorite.put(Noeud(valeur))
    
    while file_priorite.qsize() > 1:
        neud1 = file_priorite.get()
        neud2 = file_priorite.get()
        elm1 = neud1.get_valeur()
        elm2 = neud2.get_valeur()
        valeur = elm1[0] + elm2[0], elm1[1] + elm2[1]
        noeud = Noeud(valeur)
        noeud.set_gauche(neud1)
        noeud.set_droite(neud2)
        file_priorite.put(noeud)
    return file_priorite.get()
        
def creer_map(arbre, map):
    if arbre.est_feuille():
        map[arbre.get_valeur()[0]] = arbre.get_code()
    else:
        creer_map(arbre.get_gauche(), map)
        creer_map(arbre.get_droite(), map)

def coder(texte, map):
    code = ''
    for car in texte:
        code += map[car]
    return code

def decoder(code, arbre):
    arb = arbre
    texte = ''
    for car in code:
        if arb.est_feuille():
            texte += arb.get_valeur()[0]
            arb = arbre
        if car == '0':
            arb = arb.get_gauche()
        else:
            arb = arb.get_droite()
    return texte
texte = 'this is an example of a huffman tree.'
freq = calculer_frequence(texte)
map = {}
arbre = creer_arbre(freq)
creer_map(arbre, map)        
code = coder(texte, map)
                    
def codage_uniare(N, k):
    base = 2
    i = 0
    while True:
        reste = (N // (base ** i)) % base
        cu = str(rest) + cu
        i += 1
        if i > k:
            break