"""
Objectif du test :
"""
from testlib import Test
import numpy as np

class TestTpN2(Test):
    def test_produit(self):
        outc = np.array(produit(A, B))
        outa = np.array(A) * np.array(B)
        self.egalite(outc, outa)
    
    def test_produit(self):
        outc = np.array(produit_mat(A, B))
        outa = np.dot(np.array(A) * np.array(B))
        self.egalite(outc, outa)
    
    def test_transposer(self):
        outc = np.array(transposer(A))
        outa = np.transpose(A)
        self.egalite(outc, outa)



    