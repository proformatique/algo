class varlist:
    def __init__(self, data, ok=True, s=False):
        self.datanames = data
        self.started = False
        self.ok = ok
        self.show = s
        self.data = []
        self.line = self.getNames().replace(',', ' = {}</th><th>')
        self.line = '<table border=1 style="border-collapse: collapse;border: solid 1px gray"><tr><th>' + self.line  +' = {}</th></tr>'
        dv = eval(self.getNames())
        self.line = self.line.format(*dv)
    
    def setCode(self, code):
        self.code = code
    
    def getGui(self):
        print(self.data)
        for dv in self.data:
            space = ('.',) * len(dv)
            ln = "<td>{!s}</td>" * len(dv)
            ln = "<tr>"+ ln + "</tr>"
            val = dv if self.show  else space
            ln = ln.format(*val)
            self.line += ln 
        self.line += '</table>'
        return self.line 
        
    def getNames(self):
        return self.datanames
        
    def getValues(self):
        return eval(self.datanames)
    
    def withinloop(self):
        dv = self.getValues()
        self.data.append(dv)
    
    def save(self, mode):
        mode = "w" if mode else "a"
        t = "<table><tr><td><pre>{}</pre></td><td>{}</td></tr></table>"
        t = t.format(self.code, self.getGui())
        with open("fiche.html", mode) as f:
            f.write(t)
            



##
n = 5212
chiffre = None
nspy = varlist("n>0,n,chiffre") 
code ="""
n = 5212
chiffre = None
while n > 0:
    chiffre = n % 10
    n //= 10
    print(chiffre)
"""

d = code+'    nspy.withinloop()'
exec(d)
nspy.setCode(code)
nspy.save(True)
        
 ##       
 
i = None
P = 0
A = -6
B = 2

    
nspy = varlist("A,B,i,P", s=True)
code ="""
if A < 0:
    B = -B
    A = -A
for i in range(1, A+1):
    P += B
"""
pc = u"""
P <-- 0
si A < 0 alors
    B <-- -B
    A <-- -A
finsi
pour i de 1 à A faire
    P <-- P + B
finpour
"""
d = code+'    nspy.withinloop()'
exec(d)
nspy.setCode(pc)
nspy.save(True)
##
A = False
B = False
C = False

    
nspy = varlist("A,B,C", s=True)
code ="""
A = not B; nspy.withinloop()
B = not A; nspy.withinloop()
C = (not A) and B; nspy.withinloop()
A = (A or B) and not C; nspy.withinloop()
A = (not B) or (not A); nspy.withinloop()

"""
pc = u"""
P <-- 0
si A < 0 alors
    B <-- -B
    A <-- -A
finsi
pour i de 1 à A faire
    P <-- P + B
finpour
"""
d = code+'    nspy.withinloop()'
exec(d)
nspy.setCode(pc)
nspy.save(True)