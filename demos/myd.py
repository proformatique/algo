import sys
from os.path import dirname, realpath
from os import listdir
from IPython.lib.demo import Demo

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
demos = [file for file in listdir(pth) if file.startswith('demo')]
choix = menu('Demos', demos, 'Choisissez la demo : ')
suivant = Demo(demos[choix])
