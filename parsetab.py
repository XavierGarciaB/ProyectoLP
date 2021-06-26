
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALERT AMPERSAND BARRA BEGIN BEGIN_M CIRCUMFLEX COLON COMBCOMP COMMA COMMENT CONSTANT DEF DELETE DIVASSIGN DIVIDE DOBLEQUOTE DOT DOUBLEAMPERSAND DOUBLEEQUAL DOUBLELESSTHAN DOUBLEPIPE ELSE ELSEIF END END_M EQUAL EXCLAMATION EXPASSIGN FALSE FLOAT FOR GETS GREATERTHAN GREQUAL IF IN INCLUDE KEYS LBRACKET LCURLYBRACKET LEQUAL LESSTHAN LOCALVAR LPARENTHESES MINASSIGN MINUS MODASSIGN MULTIPLY NIL NOT NOTEQUAL NUMBER OR PERCENTAGE PLUS PLUSASSIGN PRINT PUTS QUESTIONMARK QUESTIONMARKPERIOD RANGEINCLUSIVE RANGEXCLUSIVE RBRACKET RCURLYBRACKET RETURN RPARENTHESES SEMICOLON SINGLEQUOTE STRING TIMESASSIGN TRIPLEEQUAL TRUE TWOGREATERTHAN TWOPOINTS TWOSTARS UNTIL VAR WAVEinicio : declaracion\n            | loop\n            | impresion\n            | funcion funcion : DEF LOCALVAR LPARENTHESES argumentos RPARENTHESES cuerpo END\n                | DEF LOCALVAR LPARENTHESES argumentos RPARENTHESES cuerpo retornar ENDargumentos : variosargumentos\n                   | MULTIPLY LOCALVAR\n                   | TWOSTARS LOCALVAR\n                   | LOCALVAR EQUAL LCURLYBRACKET RCURLYBRACKET\n                   | LOCALVAR TWOPOINTS datosvariosargumentos : LOCALVAR\n                         | LOCALVAR EQUAL datos\n                         | LOCALVAR masargumentos\n                         | LOCALVAR EQUAL datos masargumentosmasargumentos : COMMA variosargumentosretornar : RETURN LOCALVAR\n                | RETURN datosloop : FOR LOCALVAR IN rango cuerpo ENDdeclaracion : tiposvariables EQUAL datos\n                   | tiposvariables EQUAL estructurastiposvariables : VAR\n                  | LOCALVAR\n                  | CONSTANTdatos : NUMBER\n              | FLOAT\n              | STRING variables : NUMBER\n              | FLOAT\n              | STRING estructuras : hashcuerpo : declaracion\n              | loop\n              | impresionhash : LCURLYBRACKET elementoHash RCURLYBRACKET masopcioneselementoHash : variables EQUAL GREATERTHAN variables maselementosmaselementos :\n                | COMMA elementoHash maselementosmasopciones :\n                   | VAR DOT funcionesHash masopcionesfuncionesHash : INCLUDE QUESTIONMARK LPARENTHESES variables RPARENTHESES\n                     | DELETE LPARENTHESES variables RPARENTHESES\n                     | KEYSrango : NUMBER RANGEINCLUSIVE NUMBER\n              | NUMBER RANGEXCLUSIVE NUMBERimpresion : PUTS datos\n                 | PRINT datos'
    
_lr_action_items = {'FOR':([0,33,52,59,60,],[7,7,7,-44,-45,]),'PUTS':([0,33,52,59,60,],[9,9,9,-44,-45,]),'PRINT':([0,33,52,59,60,],[10,10,10,-44,-45,]),'DEF':([0,],[11,]),'VAR':([0,33,40,52,59,60,75,78,92,93,],[12,12,56,12,-44,-45,56,-43,-42,-41,]),'LOCALVAR':([0,7,11,27,33,38,39,51,52,59,60,74,],[8,15,21,35,8,53,54,65,8,-44,-45,82,]),'CONSTANT':([0,33,52,59,60,],[13,13,13,-44,-45,]),'$end':([1,2,3,4,5,16,17,18,19,20,22,23,24,40,55,58,72,75,78,81,84,92,93,],[0,-1,-2,-3,-4,-46,-25,-26,-27,-47,-20,-21,-31,-39,-35,-19,-5,-39,-43,-6,-40,-42,-41,]),'EQUAL':([6,8,12,13,29,30,31,32,35,65,],[14,-23,-22,-24,41,-28,-29,-30,48,71,]),'NUMBER':([9,10,14,25,26,46,47,48,49,57,71,74,80,86,88,],[17,17,17,30,34,59,60,17,17,30,17,17,30,30,30,]),'FLOAT':([9,10,14,25,48,49,57,71,74,80,86,88,],[18,18,18,31,18,18,31,18,18,31,31,31,]),'STRING':([9,10,14,25,48,49,57,71,74,80,86,88,],[19,19,19,32,19,19,32,19,19,32,32,32,]),'LCURLYBRACKET':([14,48,],[25,61,]),'IN':([15,],[26,]),'END':([16,17,18,19,20,22,23,24,40,42,43,44,45,55,58,66,73,75,78,82,83,84,92,93,],[-46,-25,-26,-27,-47,-20,-21,-31,-39,58,-32,-33,-34,-35,-19,72,81,-39,-43,-17,-18,-40,-42,-41,]),'RETURN':([16,17,18,19,20,22,23,24,40,43,44,45,55,58,66,75,78,84,92,93,],[-46,-25,-26,-27,-47,-20,-21,-31,-39,-32,-33,-34,-35,-19,74,-39,-43,-40,-42,-41,]),'COMMA':([17,18,19,30,31,32,35,62,65,68,79,87,90,],[-25,-26,-27,-28,-29,-30,51,51,51,80,-36,80,-38,]),'RPARENTHESES':([17,18,19,30,31,32,35,36,37,50,53,54,62,63,64,65,69,70,89,91,],[-25,-26,-27,-28,-29,-30,-12,52,-7,-14,-8,-9,-13,-11,-16,-12,-10,-15,92,93,]),'LPARENTHESES':([21,77,85,],[27,86,88,]),'MULTIPLY':([27,],[38,]),'TWOSTARS':([27,],[39,]),'RCURLYBRACKET':([28,30,31,32,61,68,79,87,90,],[40,-28,-29,-30,69,-37,-36,-37,-38,]),'RANGEINCLUSIVE':([34,],[46,]),'RANGEXCLUSIVE':([34,],[47,]),'TWOPOINTS':([35,],[49,]),'GREATERTHAN':([41,],[57,]),'DOT':([56,],[67,]),'INCLUDE':([67,],[76,]),'DELETE':([67,],[77,]),'KEYS':([67,],[78,]),'QUESTIONMARK':([76,],[85,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'declaracion':([0,33,52,],[2,43,43,]),'loop':([0,33,52,],[3,44,44,]),'impresion':([0,33,52,],[4,45,45,]),'funcion':([0,],[5,]),'tiposvariables':([0,33,52,],[6,6,6,]),'datos':([9,10,14,48,49,71,74,],[16,20,22,62,63,62,83,]),'estructuras':([14,],[23,]),'hash':([14,],[24,]),'elementoHash':([25,80,],[28,87,]),'variables':([25,57,80,86,88,],[29,68,29,89,91,]),'rango':([26,],[33,]),'argumentos':([27,],[36,]),'variosargumentos':([27,51,],[37,64,]),'cuerpo':([33,52,],[42,66,]),'masargumentos':([35,62,65,],[50,70,50,]),'masopciones':([40,75,],[55,84,]),'retornar':([66,],[73,]),'funcionesHash':([67,],[75,]),'maselementos':([68,87,],[79,90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> declaracion','inicio',1,'p_inicio','sintactico.py',5),
  ('inicio -> loop','inicio',1,'p_inicio','sintactico.py',6),
  ('inicio -> impresion','inicio',1,'p_inicio','sintactico.py',7),
  ('inicio -> funcion','inicio',1,'p_inicio','sintactico.py',8),
  ('funcion -> DEF LOCALVAR LPARENTHESES argumentos RPARENTHESES cuerpo END','funcion',7,'p_funcion','sintactico.py',11),
  ('funcion -> DEF LOCALVAR LPARENTHESES argumentos RPARENTHESES cuerpo retornar END','funcion',8,'p_funcion','sintactico.py',12),
  ('argumentos -> variosargumentos','argumentos',1,'p_argumentos','sintactico.py',15),
  ('argumentos -> MULTIPLY LOCALVAR','argumentos',2,'p_argumentos','sintactico.py',16),
  ('argumentos -> TWOSTARS LOCALVAR','argumentos',2,'p_argumentos','sintactico.py',17),
  ('argumentos -> LOCALVAR EQUAL LCURLYBRACKET RCURLYBRACKET','argumentos',4,'p_argumentos','sintactico.py',18),
  ('argumentos -> LOCALVAR TWOPOINTS datos','argumentos',3,'p_argumentos','sintactico.py',19),
  ('variosargumentos -> LOCALVAR','variosargumentos',1,'p_varios_argumentos','sintactico.py',22),
  ('variosargumentos -> LOCALVAR EQUAL datos','variosargumentos',3,'p_varios_argumentos','sintactico.py',23),
  ('variosargumentos -> LOCALVAR masargumentos','variosargumentos',2,'p_varios_argumentos','sintactico.py',24),
  ('variosargumentos -> LOCALVAR EQUAL datos masargumentos','variosargumentos',4,'p_varios_argumentos','sintactico.py',25),
  ('masargumentos -> COMMA variosargumentos','masargumentos',2,'p_masargumentos','sintactico.py',28),
  ('retornar -> RETURN LOCALVAR','retornar',2,'p_retornar','sintactico.py',31),
  ('retornar -> RETURN datos','retornar',2,'p_retornar','sintactico.py',32),
  ('loop -> FOR LOCALVAR IN rango cuerpo END','loop',6,'p_loop_for','sintactico.py',35),
  ('declaracion -> tiposvariables EQUAL datos','declaracion',3,'p_declaracion','sintactico.py',38),
  ('declaracion -> tiposvariables EQUAL estructuras','declaracion',3,'p_declaracion','sintactico.py',39),
  ('tiposvariables -> VAR','tiposvariables',1,'p_tiposvariables','sintactico.py',42),
  ('tiposvariables -> LOCALVAR','tiposvariables',1,'p_tiposvariables','sintactico.py',43),
  ('tiposvariables -> CONSTANT','tiposvariables',1,'p_tiposvariables','sintactico.py',44),
  ('datos -> NUMBER','datos',1,'p_datos','sintactico.py',46),
  ('datos -> FLOAT','datos',1,'p_datos','sintactico.py',47),
  ('datos -> STRING','datos',1,'p_datos','sintactico.py',48),
  ('variables -> NUMBER','variables',1,'p_variables','sintactico.py',51),
  ('variables -> FLOAT','variables',1,'p_variables','sintactico.py',52),
  ('variables -> STRING','variables',1,'p_variables','sintactico.py',53),
  ('estructuras -> hash','estructuras',1,'p_estructuras','sintactico.py',56),
  ('cuerpo -> declaracion','cuerpo',1,'p_cuerpo','sintactico.py',59),
  ('cuerpo -> loop','cuerpo',1,'p_cuerpo','sintactico.py',60),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','sintactico.py',61),
  ('hash -> LCURLYBRACKET elementoHash RCURLYBRACKET masopciones','hash',4,'p_hash','sintactico.py',64),
  ('elementoHash -> variables EQUAL GREATERTHAN variables maselementos','elementoHash',5,'p_elementoHash','sintactico.py',67),
  ('maselementos -> <empty>','maselementos',0,'p_maselementos','sintactico.py',70),
  ('maselementos -> COMMA elementoHash maselementos','maselementos',3,'p_maselementos','sintactico.py',71),
  ('masopciones -> <empty>','masopciones',0,'p_masopciones','sintactico.py',74),
  ('masopciones -> VAR DOT funcionesHash masopciones','masopciones',4,'p_masopciones','sintactico.py',75),
  ('funcionesHash -> INCLUDE QUESTIONMARK LPARENTHESES variables RPARENTHESES','funcionesHash',5,'p_funciones_hash','sintactico.py',78),
  ('funcionesHash -> DELETE LPARENTHESES variables RPARENTHESES','funcionesHash',4,'p_funciones_hash','sintactico.py',79),
  ('funcionesHash -> KEYS','funcionesHash',1,'p_funciones_hash','sintactico.py',80),
  ('rango -> NUMBER RANGEINCLUSIVE NUMBER','rango',3,'p_rango','sintactico.py',83),
  ('rango -> NUMBER RANGEXCLUSIVE NUMBER','rango',3,'p_rango','sintactico.py',84),
  ('impresion -> PUTS datos','impresion',2,'p_impresion','sintactico.py',88),
  ('impresion -> PRINT datos','impresion',2,'p_impresion','sintactico.py',89),
]