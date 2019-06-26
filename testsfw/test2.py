
try:
    import compression as prof
except:
    pass
try:
    import revision as prof
except:
    pass

import multiprocessing
import time
import re
from testlib import Test, mystr



class RLE_Test(Test):
    fichier = r"data\data.txt"
            
    def test_recherche(self, data):
        out = prof.recherche(RLE_Test.fichier, data)
        #out1 = prof.rle1(data)
        result = False
        point = 2
        self.total.append(point) 
        try:
            result = self.egalite(self.m.recherche(RLE_Test.fichier, data), out)
        except Exception as msg:
            self.error.append(mystr(msg))
        return result
    
    def test_inserer(self, data):
        out = prof.inserer(data[0], data[1])
        #print(out, data)
        #out1 = prof.rle1(data)
        result = False
        point = 2
        self.total.append(point) 
        try:
            result = self.egalite(self.m.inserer(data[0], data[1]), out)
        except Exception as msg:
            self.error.append(mystr(msg))
        return result
            

    def tearDown(self):
        print(self.total)