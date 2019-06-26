
import numpy as np

import multiprocessing
import time
import re
from testlib import Test, mystr



class RLE_Test(Test):
    fichier = r"data\data.txt"
            
    def test_poduit(self, data):
		A, B = data
        out = np.array(A) * np.array(B)
        #out1 = prof.rle1(data)
        result = False
        point = 2
        self.total.append(point) 
        try:
		    outc = np.array(self.m.produit(A, B))
            result = self.egalite(outc, out)
        except Exception as msg:
            self.error.append(mystr(msg))
        return result
    
    def test_produit_mat(self, data):
		A, B = data
        out = np.dot(np.array(A), np.array(B))
        #print(out, data)
        #out1 = prof.rle1(data)
        result = False
        point = 2
        self.total.append(point) 
        try:
		    outc = np.array(self.m.produit_mat(data[0], data[1]))
            result = self.egalite(outc, out)
        except Exception as msg:
            self.error.append(mystr(msg))
        return result
            

    def tearDown(self):
        print(self.total)