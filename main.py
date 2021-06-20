import ply.lex as lex

# List of token names.   This is always required

reserved = {
    #Adriana R
    'if': 'IF',
    'else': 'ELSE',
    'else if': "ELSEIF",
    'end': 'END',
    'false': 'FALSE',
    'nil': 'NIL',
    'for': 'FOR',
    #Adriana R

}

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    #Adriana Riofrio
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
    'HORZTAB',
    'VERTAB',
    'SINGLEQUOTE',
    'DOUBLEQUOTE',
    #Adriana Riofrio

) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

#Adriana Riofrio
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
t_HORZTAB = r'\\t'
t_VERTAB = r'\\v'
t_SINGLEQUOTE = r"\'"
t_DOUBLEQUOTE = r'\\"'
#Adriana Riofrio

#Adriana Riofrio
def t_VAR(t):
    r'(@{0,2}|$)[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    return t

def t_CONSTANT(t):
    r'[A-Z]+'
    t.type = reserved.get(t.value, 'CONSTANT')
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


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

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
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)

