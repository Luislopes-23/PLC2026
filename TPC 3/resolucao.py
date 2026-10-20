import re

def tpc3(texto):
    reconhecidos = []
    linha = 1
    tokens = (
        ('COMENTARIO', r'#.*'),                    
        ('NEWLINE', r'\n'),                      
        ('SKIP', r'[ \t]+'),                     
        ('PREFIXO', r'(?i:PREFIX)\b'),             
        ('SELECT', r'(?i:SELECT)\b'),
        ('WHERE', r'(?i:WHERE)\b'),
        ('OPTIONAL', r'(?i:OPTIONAL)\b'),          
        ('FILTER', r'(?i:FILTER)\b'),
        ('LIMIT', r'(?i:LIMIT)\b'),                
        ('VARIAVEL', r'\?\w+'),                    
        ('LINGUA', r'@[a-zA-Z]{2}'),               
        ('URI', r'<[^>]*>'),                       
        ('CONCEITO', r'[a-zA-Z_][a-zA-Z0-9_:]*'),  
        ('NUMERO', r'\d+'),                        
        ('STRING', r'"[^"]*"'),                    
        ('OPERADOR', r'[=!<>]+'),                  
        ('DELIMITADOR', r'[{}.;,]'),               
        ('ERRO', r'.')  
    )

    partes = []
    for nome, expressao in tokens:
        partes.append(f'(?P<{nome}>{expressao})')
        
    regex_f = '|'.join(partes)
    
    linha = 1
    reconhecidos = []
    
    for match in re.finditer(regex_f, texto):
        tipo = match.lastgroup
        valor = match.group(tipo)
        
        if tipo == 'NEWLINE':
            linha += 1
        else:
            if tipo != 'SKIP' and tipo != 'COMENTARIO':
                reconhecidos.append((tipo, valor, linha, match.span()))
                
    return reconhecidos

