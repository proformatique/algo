
class varlist:
    count = 0
    def __init__(self, data, ok=True, s=True):
        self.datanames = data
        self.started = False
        self.ok = ok
        self.show = s
        self.data = []
        self.line = self.getNames().replace(',', ' = </th><th>')
        self.line = '<table border=1 width=100% style="border-collapse: collapse;border: solid 1px gray"><tr><th>' + self.line  +' = </th></tr>'
        dv = eval(self.getNames())
        self.line = self.line.format(*dv)
        varlist.count += 1
    
    def setCode(self, code):
        self.code = code
    
    def getGui(self):
        print(self.data)
        for dv in self.data:
            space = ('.',) * len(dv)
            ln = '<td><span class="hide">{!s}</span></td>' * len(dv)
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
    
    def save(self, mode, file ="fiche.html"):
        mode = "w" if mode else "a"
        t = "<hr/><table width=100%><tr><th width=20%><h3>Listing "+str(varlist.count)+":</h3></th><th width=20%><h3>simulation d\'exécution "+str(varlist.count)+":</h3></th><th width=40%><h3>Commentaires</h3></th></tr><tr><td><pre>{}</pre></td><td>{}</td><td><hr/><br><hr/><br><hr/><br><hr/><br><hr/><br><hr/><br><hr/><br></td></tr></table>"
        t = t.format(self.code, self.getGui())
        with open(file, mode, encoding='utf-8') as f:
            f.write(t)
    
    def saveDemo(self, mode, file='demo_all.py'):
        mode = "w" if mode else "a"
        t = "# <demo> stop\n # Script \n{}"
        t = t.format(self.code)
        file = r"E:\lydex\local\algo\demos" + '\\' + file 
        with open(file, mode, encoding='utf-8') as f:
            f.write(t)
        
        
            

class filespy:
    def __init__(self, path='codes2simulate.py'):
        self.path = path
    
def purify(code, var):
    cd = code.replace('#:i', '# initialisation faite')
    cd = cd.replace(var, '')
    cd = cd.replace('#:l', '# BPoint')
    cd = cd.replace('#:v', '')
    cd = cd.replace(';', '')
    return cd

import sys
import IPython
from os.path import dirname, realpath
from os import listdir 
def menu(titre, options, message, c=1):
    print('{:*^80}'.format(titre.upper()))
    mnu = ''
    for i in range(len(options)):
        mnu+="{:2}-{:10}".format(i+1,options[i][5:-2])
        if i % c != 0:
            mnu += '\n'
    print(mnu+ '\n'+'-' * 80)
    return int(input(message + ' : ')) - 1
    
pth = realpath(dirname(sys.argv[0]))
demos = [file for file in listdir(pth) if file.startswith('code')]
choix = menu('Demos', demos, 'Choisissez la demo : ')
path = demos[choix]

with open(path) as cs:
    exec(open(path).read())
    code = cs.read().split('##:s')
    spy = [None] * len(code)
    for vi in range(len(code)):
        var = code[vi].split()
        var = var[0].replace('#:v', '')
        cd  = purify(code[vi], var)
        spy[vi] = varlist(eval(var))
        d = code[vi]
        d = d.replace('#:l', 'spy[{0}].withinloop()')
        d = d.format(vi)
        exec(d)
        spy[vi].setCode(cd)
        spy[vi].save(False)
        spy[vi].saveDemo(False)
        