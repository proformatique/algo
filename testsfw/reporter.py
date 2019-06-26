#import pdfkit
style = ["tomorrow.css","vs.css","solarized-light.css","atom-one-light.css","monokai-sublime.css"]
here = r"e:\python\git\local-repo\algo\testsfw"
def code_escape(cd):
    cd = cd.replace('<', '&lt;')
    cd = cd.replace('>', '&gt;')
    return cd

def code_lines(cd):
    if cd is None:
        return []
    cd = cd.strip()
    cl = cd.split('\n')
    return cl

def code_html_lines(cl):
    if not cl: return ""
    cdiv = "<pre><code>{}</code></pre>"
    ccntntdiv =  "</code></pre><pre><code>".join(cl)
    return cdiv.format(ccntntdiv)


    
def htmlreport(T):
    dochtml = ""
    for e in T:
        dochtml += report(e)
        # add code also dochtml += "<div><pre>{}</pre></dive>"
    classe = e.classe.upper() if e is not None else ""
    document = '''<html lang="fr"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'''
    document += '''<link rel="stylesheet" type="text/css" href="'''+here+'''\\rep\\stylereporter.css" media="all">'''
    document += '''<link rel="stylesheet" href="'''+here+'''\\rep\\styles\\'''+style[0]+'''" media="print">
<script src="'''+here+'''\\rep\\highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>'''
    document += '</head><body><h1 class="classe">{}</h1>{}</body></html>'
    document = document.format(classe, dochtml)
    return document

def html_report(T, rapport):
    document = htmlreport(T)
    with open(rapport+'.html', 'w' ,encoding='utf-8') as fd:
        fd.write(document)

def pdf_report(T, rapport):
    pdfkit.from_string(htmlreport(T), rapport+".pdf")
    
def report(eleve, note=True, desc=False, error=True, code=True, fichier=True):
    message = "<h1>{}</h1>".format(eleve.name.upper().replace('_', ' '))
    pthfichier = ""
    if note:
        message += "<h2 class=\"note hideprint\">{}/{}</h2>".format(eleve.note, sum(eleve.test.total))
    if desc and eleve.test.desc:
        message += "<h3>Description</h3><hr><div><div>{}</div></div>".format("</div><div>".join(set(eleve.test.desc)).replace('\n', '<br\>'))
    if error and eleve.test.error:
        message += '<h3>Erreurs</h3><hr><div class="errors"><div>{}</div></div>'.format("</div><div>".join(map(str,set(eleve.test.error))).replace('\n', '<br\>'))
    if fichier:
        pthfichier = "<hr># ..."+ eleve.fichier[-30:] + "<hr>"
    if code:
        code = code_escape(eleve.code)
        lignes = code_lines(code)
        precode = code_html_lines(lignes)
        message += '<h3>Code</h3>{}<div class="code">{}</div>'.format(pthfichier, precode)

    return message