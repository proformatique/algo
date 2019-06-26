import unittest
import compression as prof
import multiprocessing
import time


class RLE_Test(unittest.TestCase):
    def __init__(self, fichier):
        super()
        self.total = []
        self.desc = []
        self.name = fichier.split('\\')[-1][:-3] # nom d'eleve et du module aussi
        exec("from {} import {}".format('mpsi3g1', self.name),globals(), locals())
        #print(eval(self.name))
        self.m = eval(self.name)


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
        out1 = prof.rle1(data)
        result = False
        point = 2
        self.total.append(point) 
        try:
            result = self.assertEqual(self.m.rle(data), out)
            result = result or self.assertEqual(self.m.rle(data), out1)
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
        self.total.append(2)
        time.sleep(0.5)
        correct = True
        if p.is_alive():
            start = time.clock()
            while True:
                time.sleep(0.001)
                duree = time.clock() - start
                if duree > 2 or not p.is_alive() :
                    correct = False
                    p.terminate()
                    p.join()
                    break
            raise RuntimeError('Probleme de terminaison (boucle/recursion infinie) !')
        return correct

    
    def tearDown(self):
        print(self.total)