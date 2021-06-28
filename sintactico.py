import ply.yacc as yacc
from lexico import tokens
#Adriana Riofrio
def p_inicio(p):
    '''inicio : declaracion
            | loop
            | impresion
            | funcion '''

def p_funcion(p):
    '''funcion : DEF LOCALVAR LPARENTHESES argumentos RPARENTHESES cuerpo END
                | DEF LOCALVAR LPARENTHESES argumentos RPARENTHESES cuerpo retornar END'''

def p_argumentos(p):
    '''argumentos : variosargumentos
                   | MULTIPLY LOCALVAR
                   | TWOSTARS LOCALVAR
                   | LOCALVAR EQUAL LCURLYBRACKET RCURLYBRACKET
                   | LOCALVAR TWOPOINTS datos'''

def p_varios_argumentos(p):
    '''variosargumentos : LOCALVAR
                         | LOCALVAR EQUAL datos
                         | LOCALVAR masargumentos
                         | LOCALVAR EQUAL datos masargumentos'''

def p_masargumentos(p):
    '''masargumentos : COMMA variosargumentos'''

def p_retornar(p):
    '''retornar : RETURN LOCALVAR
                | RETURN datos'''

def p_loop_for(p):
    'loop : FOR LOCALVAR IN rango cuerpo END'

def p_declaracion(p):
    '''declaracion : tiposvariables EQUAL datos
                   | tiposvariables EQUAL estructuras'''

def p_tiposvariables(p):
    '''tiposvariables : VAR
                  | LOCALVAR
                  | CONSTANT'''
def p_datos(p):
    '''datos : NUMBER
              | FLOAT
              | STRING '''

def p_estructuras(p):
    'estructuras : hash'

def p_cuerpo(p):
    '''cuerpo : declaracion
              | loop
              | impresion'''

def p_hash(p):
    'hash : LCURLYBRACKET elementoHash RCURLYBRACKET masopciones'

def p_elementoHash(p):
    'elementoHash : datos EQUAL GREATERTHAN datos maselementos'

def p_maselementos(p):
    '''maselementos :
                | COMMA elementoHash maselementos'''

def p_masopciones(p):
    '''masopciones :
                   | LOCALVAR DOT funcionesHash masopciones'''

def p_funciones_hash(p):
    '''funcionesHash : INCLUDE QUESTIONMARK LPARENTHESES datos RPARENTHESES
                     | DELETE LPARENTHESES datos RPARENTHESES
                     | KEYS'''

def p_rango(p):
    '''rango : NUMBER RANGEINCLUSIVE NUMBER
              | NUMBER RANGEXCLUSIVE NUMBER'''


def p_impresion(p):
    '''impresion : PUTS datos
                 | PRINT datos
                 | PUTS LOCALVAR
                 | PRINT LOCALVAR
                 | PUTS masopciones
                 | PRINT masopciones'''
#Adriana Riofrio


# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")
# Build the parser

parser = yacc.yacc()
while True:
    try:
        s = input('>>')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
