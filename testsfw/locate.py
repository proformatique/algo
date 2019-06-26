def locate(filename,s): 
    assert filename and s, "invalid data"
    i = 0
    linelist = []
    try:
        with open(filename, encoding='utf-8') as fd:
            for line in fd:
                i += 1
                if s in line:
                    linelist.append(i)
    except FileNotFoundError:
        print('check your file')
    return linelist

def locate(filename,s):
    orderedlist =[]
    textfile = open( filename, 'r')
    # line = textfile.readline()
    for n, line in enumerate(textfile):
        if s in line:
            orderedlist.append(n+1)
    return orderedlist