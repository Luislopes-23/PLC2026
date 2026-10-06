import re 

def cabecalho(m):
    n = len(m.group(1))
    t = m.group(2).strip()
    return f"<h{n}>{t}</h{n}>"

def negrito(m):
    return f"<b>{m.group(1)}</b>"

def italico(m):
    return f"<i>{m.group(1)}</i>"

def listanumerada(m):
    i = m.group(0).strip().split('\n')
    html = "<ol>\n"
    for item in i:
        t= re.sub(r'^\d+\.\s+', '', item)
        html += f"<li>{t}</li>\n"
    html += "</ol>"
    return html

def link(m):
    return f"<a href=\"{m.group(2)}\">{m.group(1)}</a>"

def imagem(m):
    return f"<img src=\"{m.group(2)}\" alt=\"{m.group(1)}\"/>"

def italicoenegrito(m):
    return f"<b><i>{m.group(1)}</i></b>"

def conversor(t):

    t = re.sub(r'(?:^\d+\.\s+.+$\n?)+', listanumerada, t, flags=re.MULTILINE)
    t = re.sub(r'^(#{1,3})\s+(.+)$', cabecalho, t, flags=re.MULTILINE)
    t = re.sub(r"!\[(.*?)\]\((.*?)\)", imagem, t)
    t = re.sub(r"\[(.*?)\]\((.*?)\)", link, t)
    t = re.sub(r"\*\*\*(.*?)\*\*\*",italicoenegrito,t)
    t = re.sub(r"\*\*(.*?)\*\*", negrito, t)
    t = re.sub(r"\*(.*?)\*", italico, t)
    
    return t
