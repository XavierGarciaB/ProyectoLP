import ply.yacc as yacc
from lexico import tokens
#Adriana Riofrio
def p_inicio(p):
    '''inicio : cuerpo
              | funcion
            '''

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
def p_cuerpo(p):
    '''cuerpo : declaracion cuerpo
              | asignacion cuerpo
              | loop cuerpo
              | estructurasDatos cuerpo
              | if cuerpo
              | unless cuerpo
              | impresion cuerpo
              | operacionSet cuerpo
              | operacionarray cuerpo
              | operacionHash cuerpo
              |
              '''


def p_loop_for(p):
    'loop : FOR LOCALVAR IN rango cuerpo END'

def p_declaracion(p):
    '''declaracion : tiposvariables EQUAL datos
                   | tiposvariables EQUAL estructurasDatos
                   | tiposvariables EQUAL expresion
                   | tiposvariables EQUAL declaracion
                   '''

#nuevas reglas sintácticas SP3
####
def p_asignacion_variable(p):
    '''asignacion : LOCALVAR PLUSASSIGN datosAsignacion
                   | LOCALVAR MINASSIGN datosAsignacion
                   | LOCALVAR DIVASSIGN datosAsignacion
                   | LOCALVAR TIMESASSIGN datosAsignacion
                   | LOCALVAR MODASSIGN datosAsignacion
                   | LOCALVAR EXPASSIGN datosAsignacion'''

def p_datosAsignacion(p):
    '''datosAsignacion : number
                        | LOCALVAR'''
#####

def p_tiposvariables(p):
    '''tiposvariables : VAR
                  | LOCALVAR
                  | CONSTANT'''
def p_datos(p):
    '''datos : INTEGER
              | FLOAT
              | STRING
              '''


def p_estructurasDatos(p):
    '''estructurasDatos : hash
                        | array
                        | set '''

def p_hash(p):
    'hash : LCURLYBRACKET elementoHash RCURLYBRACKET'

#semantica para hash
def p_elementoHash(p):
    '''elementoHash : datos EQUAL GREATERTHAN datos maselementos
                     |'''

def p_maselementosHash(p):
    '''maselementos :
                | COMMA elementoHash maselementos'''

def p_hashAccess(p):
    'operacionHash : hash LBRACKET datos RBRACKET'

def p_hashAdd(p):
    'operacionHash : hash LBRACKET datos RBRACKET EQUAL datos '

def p_hashInclude(p):
    'operacionHash : hash DOT INCLUDE QUESTIONMARK LPARENTHESES datos RPARENTHESES '

def p_hashDelete(p):
    'operacionHash : hash DOT DELETE LPARENTHESES datos RPARENTHESES '

def p_hashKeys(p):
    'operacionHash : hash DOT KEYS'

def p_rango(p):
    '''rango : INTEGER RANGEINCLUSIVE INTEGER
              | INTEGER RANGEXCLUSIVE INTEGER'''

def p_impresion_puts(p):
    '''impresion : PUTS datos
                 | PUTS LOCALVAR
                 '''

def p_impresion_print(p):
    '''impresion : PRINT datos
                 | PRINT LOCALVAR
                 '''

#semantica para operaciones matematicas
def p_number(p):
    '''number : INTEGER
              | FLOAT '''

def p_expresion_factores(p):
    '''expresion : operacion
                  | LPARENTHESES operacion RPARENTHESES
                  | LPARENTHESES operacion RPARENTHESES masoperaciones'''

def p_operacion(p):
    '''operacion : number operador number
                 | operacion masoperaciones'''

def p_operaciones(p):
    '''masoperaciones : operador expresion masoperaciones
                    | operador number
                    | operador expresion
                    '''

def p_operadores_matematicos(p):
    '''operador : PLUS
                  | MINUS
                  | MULTIPLY
                  | DIVIDE
                  | PERCENTAGE'''


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

def p_operacionarray(p):
    'operacionarray : LOCALVAR LBRACKET INTEGER RBRACKET'

def p_arraynprimerosnumeros(p):
    'operacionarray : LOCALVAR DOT TAKE LPARENTHESES INTEGER RPARENTHESES '

def p_arraynultimosnumeros(p):
    'operacionarray : LOCALVAR DOT DROP LPARENTHESES INTEGER RPARENTHESES'
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
                    | datos otroElemento
                    '''


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
    "if var==5 saludo='Buenos dias' end ",
    "arreglo = [25, 54, 39]",
    "arreglo[1]",
    "arreglo.take(2)",
    "arreglo.drop(4)",
    "hash={3=>'meow', 'r'=>9.8, 3.9=>668}",
    "{3=>'meow', 'r'=>9.8, 3.9=>668}.delete(8)",
    "{3=>'meow', 'r'=>9.8, 3.9=>668}.include?(3)",
    "{3=>'meow', 'r'=>9.8, 3.9=>668}.keys",
    "var3 += 45.67",
    "var3 = (8+5+6)",
    "for x in 5..120 m1=34*34+45/89 end",
    "for x in 5..120 m1=(34.56+78-89+56+45/3-(3-4+6))+(34*23/4)/4 var4-=67 print m1 end",
    "puts 34.8",
    "var = (4-5)",
    "$variable = @var56 = var = 'meow'",
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
