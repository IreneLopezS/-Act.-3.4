import ply.lex as lex

# Lista de tokens
tokens = [
    'PR',         # Palabra Reservada
    'ID',         # Identificador
    'PA',         # Paréntesis Apertura
    'PC',         # Paréntesis Cierre
    'LLA',        # Llave Apertura
    'LLC',        # Llave Cierre
    'COMA',       # Coma
    'PUNTOCOMA',  # Punto y Coma
    'COMILLAS',   # Comillas
    'CADENA'      # Cadena de Texto
]

# Palabras reservadas
reserved = {
    'programa': 'PR',
    'suma': 'PR',
    'int': 'PR',
    'read': 'PR',
    'printf': 'PR',
    'end': 'PR'
}

# Definición de los tokens con expresiones regulares
t_PA = r'\('
t_PC = r'\)'
t_LLA = r'\{'
t_LLC = r'\}'
t_COMA = r','
t_PUNTOCOMA = r';'
t_COMILLAS = r'\"'

# Definir cómo reconocer identificadores (variables)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es palabra reservada o identificador
    return t

# Definir cómo reconocer cadenas de texto
def t_CADENA(t):
    r'\".*?\"'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Error léxico: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para ejecutar el análisis léxico
def run_lexer(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens
