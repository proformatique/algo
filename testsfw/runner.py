import os, os.path
import sys
from eleve import Eleve
from reporter import html_report, pdf_report

def file_rename(dirn, codename):
    path = os.path.join(dirn, codename)
    dest = path
    for c in "'-+, ":
        dest = dest.replace(c, '_')
    dest = dest.replace(".txt", '.py')
    dest = dest.lower()
    src = os.path.realpath(path)
    dest = os.path.realpath(dest)
    os.rename(src, dest)

def file_name(dirn, dest):
    dest = os.path.join(dirn, dest)
    return os.path.realpath(dest)
    
                        
if __name__ == "__main__":
    try:
        dirn = input("Entrer le nom du groupe : ")
        if not dirn:
            dirn = r"tsi9g9"
        listd = os.listdir(dirn)
        T = []  
        for codename in listd:
            if codename.endswith('.py'):
                file_rename(dirn, codename)
        
        listd = os.listdir(dirn) # relecutre après rename
        for codename in listd:
            if codename.endswith('.py'):
                try:
                    fichier = file_name(dirn, codename) # on ne renomme plus
                    com = "from {} import {}".format(dirn, codename[:-3])
                    try:
                        exec(com, globals(), locals())
                    except Exception as ms:
                        print(ms)
                    e = Eleve.du_fichier(fichier, dirn)
                    T.append(e)
                    try:
                        e.pass_test0()
                        e.pass_test()
                    except Exception as msg:
                        print(msg)
                    try:
                        e.pass_test2()
                    except Exception as msg:
                        print(msg)
                    e.calculer()
                except Exception as msg:
                    print(msg)#[:50]+"..."
    except Exception as ms:
        print('Le testeur encours des problèmes', ms)
    else:
        rapport = "rapport"+dirn
        html_report(T, rapport)
        # pdf_report(T, rapport)
                
