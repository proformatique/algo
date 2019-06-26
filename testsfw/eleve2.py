import re
from test import RLE_Test, mystr

CLSGRP = r'([^g]{1,2}si\d)(g\d*)'
NOM = r'\\([\D]+)[_\d]*\.py'


class Eleve:
    def __init__(self, name, classe, fichier, dirn):
        self.name = name
        self.classe = classe
        self.total = []
        self.note = 0
        self.fichier = fichier
        self.test = RLE_Test(self.fichier, dirn)
        self.code = "Pas de chance :(!"
        try:
            with open(fichier, encoding='utf-8') as f:
                self.code = f.read().strip()+'\n'
        except FileNotFoundError as msg:
            pass
        
    def __repr__(self):
        cls = self.classe
        fic = self.fichier[70:]
        nom = self.name.upper().replace('_', ' ')
        return "{} {}...{}".format(cls, nom, fic)

    def __str__(self):
        return '\n'+ self.name + "\n\t".join(self.test.desc)
        

    def du_fichier(fichier:str, dirn:str):
        rex = re.compile(CLSGRP)
        da = rex.findall(fichier)
        #print(da)
        assert da
        cls = da[0][0] or "" # if we can't get class or group
        grp = da[0][1] or ""
        rex = re.compile(NOM)
        da = rex.findall(fichier)
        #print(da)
        nm = da[0].strip('_')
        return Eleve(nm, cls, fichier, dirn)

    def calculer(self):
        total = sum(self.test.total)
        m = sum([self.test.total[i] for i in range(len(self.test.total)) if i < len(self.total) and self.total[i]])
        print('{} {}/{} {}'.format(self.name, m, total, self.fichier))
        self.note = m
        return self.note
    
    def pass_test0(self):
        dataset = ["recherche", "inserer"]
        for data in dataset:
            try:
                resultat0 = self.test.test_has_attr(data)
                self.total.append(resultat0)
                if resultat0:
                    resultat = self.test.test_has_doctest(data)
                    self.total.append(resultat)
                if resultat0:
                    resultat = self.test.test_has_doc(data)
                    self.total.append(resultat)
            except Exception as msg:
                self.test.error.append(mystr(msg))
                

    def pass_test(self):
        dataset = ["", "help", "Python", " ", "object"]
        for data in dataset:
            try:
                self.total.append(self.test.test_recherche(data))
            except Exception as msg:
                self.test.error.append(mystr(msg))
                

    def pass_test2(self):
        #print("**"*20,"\ntest2")
        dataset = [([], 2), ([1, 3], 2), ([1,2,3], 0), ([1,2,3], 3), ([1,2,3,5], 4)]
        for data in dataset:
            try:
                self.total.append(self.test.test_inserer(data))
            except Exception as msg:
                self.test.error.append(mystr(msg))


