import re



def mystr(obj):
    return "{} : {}".format(obj.__class__.__name__, obj)

# todo: dirn n'est plus utilisée?
class Test:
    def __init__(self, fichier, dirn):# dirn à revoir
        super()
        self.error = []
        self.total = []
        self.desc = []
        self.name = fichier.split('\\')[-1][:-3] # nom d'eleve et du module aussi
        exec("from {} import {}".format(dirn, self.name),globals(), locals())
        #print(eval(self.name))
        self.m = eval(self.name)
    
    def go(self):
        for attr in self.m:
            for test in dir(self):
                if test.startwith('itest'):
                    self.__getattribute__(test)(attr)
            


    def egalite(self, rc, ra):
        try:
            resultat = False
            message = "\nOn attend {} On a trouvé {}".format(ra, rc)
            assert ra == rc, message
            self.desc.append(message)
        except AssertionError as msg:
            self.error.append(mystr(msg))
        else:
            resultat = True
        return resultat
    
    def test_has_attr(self, attr):
        message = "Le module ne contient pas {}".format(attr)
        point = 3
        self.total.append(point) 
        result = attr in dir(self.m)
        if not result :
            self.error.append(message)
        return result
    
    def test_has_doc(self, attr):
        rmessage = "* {} n'est pas documenté(e)".format(attr)
        message = "Documentation de {} : {}"
        point = 3
        self.total.append(point)
        doc = ""
        try:
            ndoc = self.m.__getattribute__(attr).__doc__
            if ndoc:
                doc = ndoc
            lf = re.findall(r"[^>]+", doc)
        except Exception as msg:
            rmessage = mystr(msg)
        else:
            doc = lf[0] if len(lf) > 0 else ":( pas de chance!"
        finally:
            result = len(doc.strip()) > 20
            if not result :
                self.error.append(rmessage)
            else:
                self.desc.append(message.format(attr, doc))
        return result
    
    def test_has_doctest(self, attr):
        rmessage = "* {} n'a pas de tests".format(attr)
        message = "Nombre de tests de {} : {}"
        point = 3
        self.total.append(point) 
        doc = ""
        result = False
        try:
            ndoc = self.m.__getattribute__(attr).__doc__
            if ndoc:# on ne change pas "" par None
                doc = ndoc
        except Exception as msg:
            rmessage = mystr(msg)
        else:
            ma = re.findall(">>> "+attr, doc)
            ntests = len(ma)
            result = ntests > 0
        if result :
            self.desc.append(message.format(attr, ntests))
        else:
            self.error.append(rmessage)
        return result
