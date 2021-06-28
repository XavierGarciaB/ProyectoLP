import ply.lex as lex

# List of token names.   This is always required


reserved = {
    #Xavier Garcia
    'puts': 'PUTS',
    'gets': 'GETS',
    'print': 'PRINT',
    'BEGIN': 'BEGIN_M',
    'END': 'END_M',
    'begin': 'BEGIN',
    'def': 'DEF',
    #Xavier Garcia

    #Adriana Riofrio
    'if': 'IF',
    'else': 'ELSE',
    'else if': "ELSEIF",
    'end': 'END',
    'false': 'FALSE',
    'nil': 'NIL',
    'for': 'FOR',
    'include': 'INCLUDE',
    'delete': 'DELETE',
    'keys': 'KEYS',
    #Adriana Riofrio

    #Luis Anchundia
    'in': 'IN',
    'not': 'NOT',
    'or': 'OR',
    'return': 'RETURN',
    'true': 'TRUE',
    'until': 'UNTIL'
    #Luis Anchundia


}

tokens = (
    'NUMBER',
    #Xavier Garcia
    'EXCLAMATION',
    'PLUS',
    'MINUS',
    'WAVE',
    'MULTIPLY',
    'TWOSTARS',
    'DIVIDE',
    'PERCENTAGE',
    'DOUBLELESSTHAN',
    'TWOGREATERTHAN',
    'AMPERSAND',
    'BARRA',
    'CIRCUMFLEX',
    'DOUBLEEQUAL',
    'TRIPLEEQUAL',
    'ALERT',

    #Xavier Garcia

    #Adriana Riofrio
    'FLOAT',
    'DOT',
    'NOTEQUAL',
    'GREATERTHAN',
    'LESSTHAN',
    'EQUAL',
    'GREQUAL',
    'LEQUAL',
    'COMBCOMP',
    'PLUSASSIGN',
    'MINASSIGN',
    'MODASSIGN',
    'EXPASSIGN',
    'TIMESASSIGN',
    'DIVASSIGN',
    'RANGEINCLUSIVE',
    'RANGEXCLUSIVE',
    'CONSTANT',
    'VAR',
    'LOCALVAR',
    'STRING',
    'QUESTIONMARK',
    'TWOPOINTS',
    #Adriana Riofrio

    #Luis Anchundia
    'SINGLEQUOTE',
    'DOBLEQUOTE',
    'COLON',
    'QUESTIONMARKPERIOD',
    'DOUBLEAMPERSAND',
    'DOUBLEPIPE',
    'LPARENTHESES',
    'RPARENTHESES',
    'LBRACKET',
    'RBRACKET',
    'LCURLYBRACKET',
    'RCURLYBRACKET',
    'COMMA',
    'SEMICOLON',
    'COMMENT',
    'BOOLEAN'
    #'AZ',
    #'BACKO',
    #'BACKX',
    #'BACKU'
    #Luis Anchundia

) + tuple(reserved.values())

# Regular expression rules for simple tokens
#Xavier Garcia
t_EXCLAMATION = r'\!'
t_PLUS = r'\+'
t_MINUS = r'-'
t_WAVE = r'~'
t_MULTIPLY = r'\*'
t_TWOSTARS = r'\*\*'
t_DIVIDE = r'/'
t_PERCENTAGE = r'%'
t_DOUBLELESSTHAN = r'<<'
t_TWOGREATERTHAN = r'>>'
t_AMPERSAND = r'&'
t_BARRA = r'\|'
t_CIRCUMFLEX = r'\^'
t_DOUBLEEQUAL = r'=='
t_TRIPLEEQUAL = r'==='
#Xavier Garcia

#Adriana Riofrio
t_TWOPOINTS = r':'
t_QUESTIONMARK = r'\?'
t_DOT = r'\.'
t_NOTEQUAL = r'!='
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_EQUAL = r'='
t_GREQUAL = r'>='
t_LEQUAL= r'<='
t_COMBCOMP = r'<=>'
t_PLUSASSIGN = r'\+='
t_MINASSIGN = r'-='
t_MODASSIGN = r'%='
t_EXPASSIGN = r'\*\*='
t_TIMESASSIGN = r'\*='
t_DIVASSIGN = r'\\='
t_RANGEINCLUSIVE = r'\.\.'
t_RANGEXCLUSIVE = r'\.\.\.'
#Adriana Riofrio

#Luis Anchundia
t_SINGLEQUOTE=r'\''
t_DOBLEQUOTE=r'\"'
t_COLON=';'
t_QUESTIONMARKPERIOD='\?:'
t_DOUBLEAMPERSAND='&&'
t_DOUBLEPIPE='\|\|'
t_LPARENTHESES='\('
t_RPARENTHESES='\)'
t_LBRACKET='\['
t_RBRACKET='\]'
t_LCURLYBRACKET='\{'
t_RCURLYBRACKET='\}'
t_COMMA=','
t_SEMICOLON=';'
#Luis Anchundia


#Adriana Riofrio
def t_VAR(t):
    r'(@{1,2}|\$)[a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    return t

def t_LOCALVAR(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'LOCALVAR')  # Check for reserved words
    return t

def t_CONSTANT(t):
    r'[A-Z]+'
    t.type = reserved.get(t.value, 'CONSTANT')
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'(".*"|\'.*\')'
    t.type = reserved.get(t.value, 'STRING')
    return t


#Adriana Riofrio


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Xavier Garcia
def t_ALERT(t):
    r'"\w*\\a\w*"'
    t.value = r'\a'
    return t


def t_BACKSPACE(t):
    r'"\w*\\b\w*"'
    t.value = r'\ b'
    print(t.value)
    return t


def t_FORMFEED(t):
    r'"\w*\\f\w*"'
    t.value = r'\f'
    return t


def t_NEWLINE(t):
    r'"\w*\\n\w*"'
    t.value = r'\n'
    return t


def t_CARRIAGERETURN(t):
    r'"\w*\\r\w*"'
    t.value = r'\r'
    return t
#Xavier Garcia


#Adriana Riofrio
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\v'

literals = ["\'", '\"','\\']

def t_singlequote(t):
    r"'\\''"
    t.type = "\'"
    return t

def t_doublequote(t):
    r'"\\""'
    t.type = '\"'
    return t

def t_backslash(t):
    r'(\'\\\\\'|"\\\\")'
    t.type = '\\'
    return t
#Adriana Riofrio


#Luis Anchundia
def t_AZ(t):
    r"'\A\.\.\.\Z'"
    t.type = "\A...\Z"
    return t


def t_BACKO(t):
    r'"\w*\\o\w*"'
    t.value = r'\o'
    return t


def t_BACKU(t):
    r'"\w*\\u\w*"'
    t.value = r'\u'
    return t


def t_BACKX(t):
    r'"\w*\\x\w*"'
    t.value = r'\x'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_BOOLEAN(t):
    r'(true|false)'
    t.type = reserved.get(t.value, 'BOOLEAN')
    return t
#Luis Anchundia


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


 # Build the lexer
lexer = lex.lex()
lineas = ["{}<< + 3 - 4 = @@variable gets 'dsd4324' : ? ack true TRUE\n",'"dshdajshdwu909,."',""]
cont = 0
linea = lineas[cont]
while linea != "":
    lexer.input(linea)
    getTokens(lexer)
    cont = cont + 1
    linea = lineas[cont]
print("Succesfull")