import ply.yacc as yacc
from lexer import tokens

# Reglas de la gramática
def p_statement_for(p):
    '''statement : FOR ID EQUALS expression'''
    p[0] = "Sintácticamente correcto"

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    pass

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    p[0] = "Error sintáctico."

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para realizar el análisis sintáctico
def run_parser(data):
    result = parser.parse(data)
    if result is None:
        return "Error sintáctico."
    return result
