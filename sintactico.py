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
              | string cuerpo
              |
              '''


def p_loop_for(p):
    'loop : FOR LOCALVAR IN rango cuerpo END'

def p_declaracion(p):
    '''declaracion : tiposvariables EQUAL datos
                   | tiposvariables EQUAL estructurasDatos
                   | tiposvariables EQUAL expresion
                   | tiposvariables EQUAL declaracion
                   | tiposvariables EQUAL casting
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
#semantica para array

def p_array(p):
    '''array : LBRACKET RBRACKET
            | LBRACKET datosarray RBRACKET'''

def p_datosvarios(p):
    '''datosvarios : datos
                | number
                | VAR
                | LOCALVAR'''

def p_datosarray(p):
    ''' datosarray : datosvarios
                    | datosarray COMMA datosvarios'''

def p_operacionarrayelemento(p):
    'operacionarray : array LBRACKET INTEGER RBRACKET'

def p_arraynprimerosnumeros(p):
    'operacionarray : array DOT TAKE LPARENTHESES INTEGER RPARENTHESES '

def p_arraynultimosnumeros(p):
    'operacionarray : array DOT DROP LPARENTHESES INTEGER RPARENTHESES'

def p_arraypush(p):
    ''' operacionarray : array DOT push maspush'''
def p_push(p):
    ''' push : PUSH LPARENTHESES datosvarios RPARENTHESES
            | '''

def p_maspush(p):
    ''' maspush :
                | DOT push maspush'''
def p_arrayeliminaruno(p):
    ''' operacionarray : array DOT POP
                        | array DOT POP LPARENTHESES INTEGER RPARENTHESES'''

def p_arrayeliminarnposicion(p):
    ' operacionarray : array DOT DELETE LPARENTHESES INTEGER RPARENTHESES'

def p_arraylenght(p):
    ' operacionarray : array DOT LENGTH LPARENTHESES RPARENTHESES '


def p_arrayvacio(p):
    ' operacionarray : array DOT EMPTY QUESTIONMARK'

#semantica para if
def p_datoscompletos(p):
    ''' datoscompletos : datosvarios
                        | tiposvariables'''

def p_if(p):
    '''if : IF datoscompletos operadores datoscompletos cuerpo END
            | IF datoscompletos operadores datoscompletos cuerpo else '''

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

#Luis Anchundia


#Xavier Garcia

def p_unless(p):
    '''unless : UNLESS expresionCondicional cuerpo ELSE cuerpo END'''


# Semantica para booleanos
def p_expresionCondicional(p):
    '''expresionCondicional : boolean
                            | EXCLAMATION LPARENTHESES boolean RPARENTHESES'''


def p_operadorBinario(p):
    '''operadorBinario : DOUBLEAMPERSAND
                        | DOUBLEPIPE'''


def p_boolean(p):
    '''boolean : condiciones
                | EXCLAMATION LPARENTHESES condiciones RPARENTHESES
                | boolean operadorBinario boolean'''


def p_condiciones_var(p):
    '''condiciones : tiposvariables operadores tiposvariables'''


def p_condiciones_datos(p):
    '''condiciones : datos operadores datos'''


def p_condiciones_mix(p):
    '''condiciones : tiposvariables operadores datos
                   | datos operadores tiposvariables'''
#

# Semantica para set
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
#

# Semantica para Strings
def p_string_concat(p):
    '''string : STRING PLUS STRING'''

def p_string_repeat(p):
    '''string : STRING MULTIPLY INTEGER'''

def p_string_operations(p):
    '''string : STRING DOT stringOpt'''

def p_stringOpt(p):
    '''stringOpt : UPCASE
                    | DOWNCASE
                    | LENGTH
                    | CAPS
                    | INSERT LPARENTHESES INTEGER COMMA STRING RPARENTHESES'''

def p_casting_toInt(p):
    '''casting : STRING DOT TO_I'''

def p_casting_toFloat(p):
    '''casting : STRING DOT TO_F'''

def p_casting_toString(p):
    '''casting : number DOT TO_S'''

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
    "unless !(x===3) x=4 else x=5 end",
    "unless !(x>3 && x<10) x=11 else x=0 end",
    "unless !(x<10) || y!=5 print x else print y end",
    "valores = set[1,2]",
    "'hola' + 'mundo'",
    "'hola' * 10",
    "'hola'.upcase",
    "'HOLA MUNDO'.downcase",
    "'un perro'.capitalize",
    "'hola'.insert(0, 'H')",
    "'Una cadena de caracteres'.length",
    "x = '5'.to_i",
    "x = '134.56'.to_f",
    "x = 512.to_s",
    "x = 3.14.to_s",
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
    " [4,6,mia].push(4).push(6).push(4)",
    " [4,6,mia].pop(4)",
    "[a].delete(4)",
    "[1,2].length()",
    "[new,old].empty?",
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
