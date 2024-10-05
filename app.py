from flask import Flask, render_template, request
import ply.lex as lex
import ply.yacc as yacc

app = Flask(__name__)

# 1. Analizador Léxico (Lexer)
tokens = ['FOR', 'IDENTIFIER']

t_FOR = r'for'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter no reconocido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# 2. Analizador Sintáctico (Parser)
def p_statement_for(p):
    'statement : FOR IDENTIFIER'
    p[0] = 'Sintáctico Correcto'

def p_error(p):
    print(f"Error de sintaxis en: {p}")

parser = yacc.yacc()

@app.route("/", methods=["GET", "POST"])
def analyze():
    text = ""
    tokens = []
    syntax_result = ""
    
    if request.method == "POST":
        text = request.form["text"]
        
        # Proceso de análisis léxico
        lexer.input(text)
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append(tok)
        
        # Proceso de análisis sintáctico
        syntax_result = parser.parse(text)
    
    return render_template("index.html", text=text, tokens=tokens, syntax_result=syntax_result)

