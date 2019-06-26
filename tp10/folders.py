class afichier:
    def __init__(self, nom):
        self.nom = nom
        self.content = []
        self.parent = None
    
    def get_chemin(self):
        parent = self.get_parent()
        if parent is None:
            return self.nom
        else:
            return parent.get_chemin()+'/'+self.nom
        
    def get_nom(self):
        return self.nom
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_parent(self):
        return self.parent
    
    def get_niveau(self):
        parent = self.get_parent()
        if parent is None:
            return 0
        else:
            return parent.get_niveau() + 1

    def set_nom(self, nom):
        self.nom = nom
    
    def afficher(self):
        print(self.get_niveau()*'\t', self.nom,'({})'.format(self.get_chemin()))


class fichier(afichier):
    pass


class dossier(afichier):
    def set_content(self, fldrs):
        for e in fldrs:
            e.set_parent(self)
            self.content.append(e)
    
    def afficher(self):
        super().afficher()
        nd = 0
        nf = 0
        for e in self.content:
            n = e.afficher()
            if n is None:
                nf += 1
            else:
                nd += 1 + n[0]
                nf = nf + n[1]
        if self.get_niveau() == 0:
            print('({} dossiers, {} fichiers)'.format(nd,nf))
        else:
            return nd, nf 
                

f1 = [fichier('fichier{}.txt'.format(i+1)) for i in range(10)]
a = dossier('a')
a.set_content(f1[:2])
b = dossier('b')
b.set_content([f1[2]])
c = dossier('c')
c.set_content([f1[3]])
dir1 = dossier('dir1')
dir1.set_content([a, b, c])
a = dossier('a')
a.set_content(f1[4:6])
b = dossier('b')
b.set_content(f1[6:8])
c = dossier('c')
c.set_content(f1[8:10])
dir2 = dossier('dir2')
dir2.set_content([a, b, c])
courant = dossier('.')
courant.set_content([dir1, dir2])