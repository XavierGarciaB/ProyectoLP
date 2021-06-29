import ply.yacc as yacc
from lexico import tokens
#Adriana Riofrio
def p_inicio(p):
    '''inicio : declaracion
            | loop
            | impresion
            | funcion
            | if
            | array
            | accederarray
            | unless
            | set
            | operacionSet '''

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
    '''estructuras : hash
                    | set'''

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


def p_impresion_puts(p):
    '''impresion : PUTS datos
                 | PUTS LOCALVAR
                 | PUTS masopciones'''


def p_impresion_print(p):
    '''impresion : PRINT datos
                 | PRINT LOCALVAR
                 | PRINT masopciones'''
#Adriana Riofrio

#Luis Anchundia
def p_array(p):
    '''array : tiposvariables EQUAL LBRACKET datosarray RBRACKET
                | tiposvariables EQUAL LBRACKET RBRACKET'''

def p_if(p):
    '''if : IF datosvarios operadores datosvarios cuerpo END
            | IF datosvarios operadores datosvarios cuerpo else '''

def p_else(p):
    'else : ELSE cuerpo END'

def p_operadores(p):
    '''operadores : DOUBLEEQUAL
                 | TRIPLEEQUAL
                 | GREATERTHAN
                 | NOTEQUAL
                 | LESSTHAN
                 | GREQUAL
                 | LEQUAL'''
def p_datosvarios(p):
    '''datosvarios : datos
                | tiposvariables'''
def p_datosarray(p):
    '''datosarray : datosvarios
                    | datosarray COMMA datosvarios'''

def p_accederarray(p):
    'accederarray : tiposvariables LBRACKET NUMBER RBRACKET'

#Luis Anchundia


#Xavier Garcia
def p_unless(p):
    '''unless : UNLESS condiciones cuerpo ELSE cuerpo END'''


def p_condiciones_var(p):
    '''condiciones : tiposvariables operadores tiposvariables'''


def p_condiciones_datos(p):
    '''condiciones : datos operadores datos'''


def p_condiciones_mix(p):
    '''condiciones : tiposvariables operadores datos
                   | datos operadores tiposvariables'''


def p_set(p):
    '''set : SET LBRACKET  elementoSet RBRACKET'''


def p_elementoSet(p):
    '''elementoSet :
                    | datos
                    | tiposvariables
                    | datos otroElemento
                    | tiposvariables otroElemento'''


def p_otroElemento(p):
    '''otroElemento :
                | COMMA elementoSet otroElemento'''


def p_operacionSet_agregar(p):
    '''operacionSet : set DOT ADD LPARENTHESES datos RPARENTHESES
                    | set DOT ADD LPARENTHESES tiposvariables RPARENTHESES'''


def p_operacionSet_limpiar(p):
    '''operacionSet : set DOT CLEAR'''


def p_operacionSet_eliminar(p):
    '''operacionSet : set DOT DELETE LPARENTHESES datos RPARENTHESES
                    | set DOT DELETE LPARENTHESES tiposvariables RPARENTHESES'''

#Xavier Garcia


# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")
# Build the parser


parser = yacc.yacc()

pruebas = [
    "unless x===3 x=10 else x=20 end",
    "valores = set[1,2]",
    "set[1,2].add(3)",
    "set[1,2].delete(1)",
    "set[1,2].clear",
    ""
]


print("ALGORITMO DE PRUEBAS")
cont = 0
linea = pruebas[cont]
while linea != "":
    #try:
    #    s = input('>>')
    #except EOFError:
    #    break
    #if not s: continue
    print(linea)
    result = parser.parse(linea)
    print(result)
    cont = cont + 1
    linea = pruebas[cont]
