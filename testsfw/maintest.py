"""
TEST la la boucle est bien passé à verifier
GENERATION DE RAPPORT

"""

import unittest
import compression as prof
import imp
import multiprocessing
import time
import re
import os, os.path
import sys
sys.path.append([r'E:\lydex\local\algo\innovation\mpsi3g1'])
CLSGRP = r'([^g]{1,2}si\d)(g\d*)'
NOM = r'\\([\D]+)[_\d]*\.py'


class Eleve:
    def __init__(self, name, classe, fichier):
        self.name = name
        self.classe = classe
        self.total = []
        self.fichier = fichier
        self.dataset = ["", "ababa", "ababaababab", "jjjjjjjjjjjjjjjjjjjj", "'             '"
         "eeeeeeuuuuuuuuuuuuiiiiiiiiiiizzzz"]
        self.test = RLE_Test(self.fichier)
    
    def __repr__(self):
        cls = self.classe
        fic = self.fichier[70:]
        nom = self.name.upper().replace('_', ' ')
        return "{} {}...{}".format(cls, nom, fic)

    def __str__(self):
        return '\n'+ self.name + "\n\t".join(self.test.desc)

    def du_fichier(fichier:str):
        rex = re.compile(CLSGRP)
        da = rex.findall(fichier)
        #print(da)
        assert da
        cls = da[0][0]
        grp = da[0][1]
        rex = re.compile(NOM)
        da = rex.findall(fichier)
        #print(da)
        nm = da[0].strip()
        return Eleve(nm, cls, fichier)

    def calculer(self):
        total = sum(self.test.total)
        m = sum([self.test.total[i] for i in range(len(self.test.total)) if self.total[i]])
        print('{} {}/{}'.format(self.name, m, total))
        return m / total

    def pass_test(self):
        for data in self.dataset:
            try:
                self.total.append(self.test.test_rle(data))
            except Exception as msg:
                self.test.desc.append(msg)
                

    def pass_test2(self):
        for data in self.dataset:
            try:
                self.total.append(self.test.test_il_decompression_rle(data))
            except Exception as msg:
                self.test.desc.append(msg)


class RLE_Test(unittest.TestCase):
    def __init__(self, fichier):
        super()
        self.total = []
        self.desc = []
        name = fichier.split('\\')[-1][:-3] # nom d'eleve et du module aussi
        self.m = eval(name)


    def assertEqual(self, rc, ra):
        try:
            resultat = False
            message = "\nOn attend {} On a trouvé {}".format(ra, rc)
            assert ra == rc, message
        except AssertionError as msg:
            self.desc.append(str(msg))
        else:
            resultat = True
        return resultat
    
    def assertTrue(self, data):
        try:
            out = self.m.decompression_rle(self.m.rle(data))
            resultat = False
            message = "\nAttendu : {} On a trouvé : {}".format(data, out)
            assert out == data, message
        except AssertionError as msg:
            self.desc.append(str(msg))
        else:
            resultat = True
        return resultat
        
    def test_rle(self, data):
        out = prof.rle(data)
        result = False
        point = 2
        self.total.append(point) 
        try:
            result = self.assertEqual(self.m.rle(data), out)
        except Exception as msg:
            self.desc.append(str(msg))
        return result
    
    def test_rle1(self, data):
        result = False
        point = 2
        self.total.append(point) 
        try:
            return self.assertTrue(data)
        except Exception as msg:
            self.desc.append(str(msg))
        return result
            
    
    def test_il_decompression_rle(self, data):
        p = multiprocessing.Process(target=self.m.decompression_rle, args=(data,))
        p.start()
        time.sleep(1)
        self.total.append(2)
        correct = True
        if p.is_alive():
            start = time.clock()
            while True:
                time.sleep(0.01)
                duree = time.clock() - start
                if duree > 1 or not p.is_alive() :
                    correct = False
                    p.terminate()
                    p.join()
                    break
            raise RuntimeError('Probleme de terminaison (boucle/recursion infinie) !')
        return correct

    
    def tearDown(self):
        print(self.total)

def file_name(dir, codename):
    path = dirn+os.sep+codename
    dest = path.replace(' ', '_')
    dest = dest.replace('-', '_')
    dest = dest.lower()
    src = os.path.realpath(path)
    dest = os.path.realpath(dest)
    os.rename(src, dest)
    return dest
    
if __name__ == "__main__":
    try:
        dirn = r"mpsi3g1"
        listd = os.listdir(dirn)
        T = []
        for codename in listd:
            if codename.endswith('.py'):
                try: # 0645006010
                    exec("from {} import {}".format(dirn, codename[:-3]))
                    fichier = file_name(dirn, codename)
                    #print(fichier)
                    e = Eleve.du_fichier(fichier)
                    T.append(e)
                    e.pass_test()
                    e.pass_test2()
                    e.calculer()
                    
                except Exception as msg:
                    print(msg)
    except Exception as ms:
        print('Le testeur encours des problèmes', ms)