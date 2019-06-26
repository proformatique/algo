"""
<head>
<link rel="stylesheet" href="sim.css" type="text/css" media="screen" />
<link rel="stylesheet" href="simhide.css" type="text/css" media="print" />
</head>
TAF 1 :
Sans utiliser la machine:
<ol>
<li>Exécutez manuellement les instructions du script</li>
<li>Remplissez le tableau de simulation (à chaque break Point)</li>
<li>Notez vos remarques et commentaires</li>
<li>Dites ce que fait le script</li>
</ol>
TAF 2 :
En utilisant la machine:
<ol>
<li>Exécutez le script, après avoir remplacé # BPoint par l'instruction print()</li>
<li>Comparez votre tableau de simulation avec le résultat de l'éxecution</li>
<li>Notez vos remarques et commentaires</li>
<li>Transformez le script en sous-programme def identifiant(params)</li>
</ol>
"""


class varlist:
    seps = '##s:'
    sepi = '#i:'
    sepl = '#bp:'
    sepl2 = '##bp:'
    sepv = '#v:'
    sepa = '#A:'
    webdist = './dist/'
    demodist = r"E:\lydex\local\algo\demos" + '\\'
    src = './source/'

    count = 0
    def __init__(self, data, ok=True, s=True):
        self.datanames = data
        self.started = False
        self.ok = ok
        self.show = s
        self.data = []
        self.line = self.getNames().replace(',', ' = </th><th>')
        self.line = '<table border=1 style="border-collapse: collapse;border: solid 1px gray"><tr><th>' + self.line  +' = </th></tr>'
        dv = eval(self.getNames())
        #todo self.line = self.line.format(*dv)
        #self.line %= tuple(dv)
        varlist.count += 1
    
    def setCode(self, code):
        self.code = code
    
    def getGui(self):
        for dv in self.data:
            space = ('.',) * len(dv)
            ln = '<td><span class="hide">%s</span></td>' * len(dv)
            ln = "<tr>"+ ln + "</tr>"
            val = dv if self.show  else space
            #todo ln = ln.format(*val)
            ln %= val
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
        t = "<hr/><table ><tr><th class=code><h3>Listing "+str(varlist.count)+":</h3></th><th class=sim ><h3>simulation d\'exécution "+str(varlist.count)+":</h3></th><th class=com ><h3>Commentaires</h3></th></tr><tr><td><pre>%s</pre></td><td>%s</td><td><hr/><br><hr/><br><hr/><br><hr/><br><hr/><br><hr/><br><hr/><br></td></tr></table>"
        t %= (self.code, self.getGui()) #todo t.format(self.code, self.getGui())
        file = varlist.webdist + file
        with open(file, mode, encoding='utf-8') as f:
            f.write(t)
    
    def saveDemo(self, mode, file='demo_all.py'):
        mode = "w" if mode else "a"
        t = "\n# <demo> stop\n # Script \n %s" #todo  {}
        cd = self.code.replace("# APPEL", '\n# <demo> stop\n# APPEL')
        t %= cd #todo t.format(cd)
        file = varlist.demodist + file 
        with open(file, mode, encoding='utf-8') as f:
            f.write(t)
        
        
            

class filespy:
    def __init__(self, path='codes2simulate.py'):
        self.path = path
    
def purify(code, var):
    cd = code.replace(varlist.sepi, '# Initialisation faite')
    cd = cd.replace(var, '')
    cd = cd.replace(varlist.sepl2, '# BPoint')
    cd = cd.replace(varlist.sepl, '# BPoint')
    cd = cd.replace(varlist.sepv, '')
    cd = cd.replace(varlist.sepa, '# APPEL')
    return cd

import sys
import IPython
from os.path import dirname, realpath
from os import listdir 
def menu(titre, options, message, c=1):
    print('{:*^40}'.format(titre.upper()))
    mnu = ''
    for i in range(len(options)):
        mnu+="{:2}-{:10}".format(i+1,options[i][6:-3])
        if i % c != 0:
            mnu += '\n'
    print(mnu+ '\n'+'-' * 40)
    try:
        return int(input(message + ' : ')) - 1
    except:
        return -1
    
pth = realpath(dirname(sys.argv[0])) + varlist.src
demos = [file for file in listdir(pth) if file.startswith('code')]
if demos:
    while True:
        choix = menu('SOURCES', demos, 'Choisissez la source ')
        if choix < 0 or choix >= len(demos):
            if input('Voulez-vous quitter? (y/n) ') != 'n':
                print('Ok! bye')
                break 
        else:
            path = demos[choix] 
            with open(varlist.src + path) as cs:
                exec(open(varlist.src + path).read())
                code = cs.read().split(varlist.seps)
                spy = [None] * len(code)
                for vi in range(len(spy)):
                    var = code[vi].split()
                    var = var[0].replace(varlist.sepv, '')
                    cd  = purify(code[vi], var)
                    spy[vi] = varlist(eval(var)) # Todo creation 
                    d = code[vi]
                    d = d.replace(varlist.sepl2, '; spy[%(s)s].withinloop()')
                    d = d.replace(varlist.sepl, 'spy[%(s)s].withinloop()')
                    d %= {'s':vi} # d.format(vi)
                    exec(d)
                    spy[vi].setCode(cd)
                    spy[vi].save(False, file=path[:-3] + ".html")
                    spy[vi].saveDemo(False, file="demo_" + path[5:])
else:
    print('Pas de sources')

