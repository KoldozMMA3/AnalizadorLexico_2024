import ply.lex as lex

# Palabras reservadas
reserved = {
    'Proceso': 'Inicio_Proceso',
    'FinProceso': 'Fin_Proceso',
    'si': 'Condiciones_Si',
    'sino': 'Condiciones_Sino',
    'finSi': 'Condiciones_FinSi',
    'mientras': 'Bucle',
    'imprimir': 'Impresor',
    'entero': 'Dato_Entero',
    'largo': 'Dato_Largo',
    'flotante': 'Dato_Flotante',
    'caracter': 'Dato_Caracter',
    'booleano': 'Dato_Booleano',
    'Funcion': 'Dato_Funcion',
    'regresa': 'Regresa',
}

# Lista de tokens
tokens = [
    'Identificador', 'Num_Entero', 'Num_Decimales', 'Op_Suma', 'Op_Resta',
    'Op_Multiplicacion', 'Op_Division', 'Mayor_Q', 'Menor_Q', 'Igualdad',
    'Comparacion', 'Mayor_Igual', 'Menor_Igual', 'Incremento',
    'Comparacion_Igualdad', 'Op_Logico', 'Sum_Asignacion', 'Decremento',
    'Cadena_Texto', 'Comentario', 'Inicio_Parentesis', 'Fin_Parentesis',
    'Parentesis_Abrir', 'Parentesis_Cerrar', 'Llave_Abrir', 'Llave_Cerrar',
    'Coma', 'Punto', 'Punto_Coma', 'Inicio_comentario', 'Fin_comentario'
] + list(reserved.values())

# Expresiones regulares para los tokens
t_Op_Suma = r'\+'
t_Op_Resta = r'-'
t_Op_Multiplicacion = r'\*'
t_Op_Division = r'%|/'
t_Mayor_Q = r'>'
t_Menor_Q = r'<'
t_Igualdad = r'='
t_Comparacion = r'=='
t_Mayor_Igual = r'>='
t_Menor_Igual = r'<='
t_Incremento = r'\+\+'
t_Comparacion_Igualdad = r'!='
t_Op_Logico = r'OR'
t_Sum_Asignacion = r'\+='
t_Decremento = r'--'
t_Parentesis_Abrir = r'\('
t_Parentesis_Cerrar = r'\)'
t_Llave_Abrir = r'\{'
t_Llave_Cerrar = r'\}'
t_Coma = r'\,'
t_Punto = r'\.'
t_Punto_Coma = r'\;'
t_Inicio_comentario = r'\.\*'
t_Fin_comentario = r'\*\.'


# Regla para manejar identificadores
def t_Identificador(t):
  r'[_a-zA-Z][_a-zA-Z0-9]*'
  t.type = reserved.get(t.value,
                        'Identificador')  # Verificar palabras reservadas
  return t


def t_Num_Decimales(t):
  r'\d+\.\d+'
  t.value = float(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


def t_Num_Entero(t):
  r'\d+'
  t.value = int(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


# Definir una regla para que podamos rastrear los números de línea
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# Una cadena que contiene caracteres ignorados (espacios y tabulaciones)
t_ignore = ' \t'


# Regla de manejo de errores
def t_error(t):
  print("Caracter Incorecto no encontrado '%s'" % t.value[0])
  t.lexer.skip(1)


# Regla para manejar comentarios
def t_Comentario(t):
  r'\./.*?/\.'
  return t  # Los comentarios se ignorarán


# Regla para manejar cadenas de texto
def t_Cadena_Texto(t):
  r'"([^"\\]|\\.)*"'
  t.value = str(t.value)
  return t


# Build the lexer
lexer = lex.lex()

file_path = 'ejemplo.txt'
with open(file_path, 'r') as file:
  data = file.read()

lexer.input(data)


class Token:

  def __init__(self, type, lexeme, line, column):
    self.type = type
    self.lexeme = lexeme
    self.line = line
    self.column = column


tokens = []

while True:
  tok = lexer.token()
  if not tok:
    break

  t = Token(tok.type, tok.value, tok.lineno, tok.lexpos)
  tokens.append(t)

for token in tokens:
  print("TIPO:", token.type, 
        "LEXEMA:", token.lexeme, 
        "LINEA:", token.line,
        "COLUMNA:", token.column)
