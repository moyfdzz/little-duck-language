# -----------------------------------------------------------------------------
# Moisés Fernández Zárate A01197049
# littleducklex.py
#
# Little Duck Language 2020 parser with python using PLY (Python Lex Yacc).
# -----------------------------------------------------------------------------

import sys
import ply.yacc as yacc
from littleducklex import tokens

# Programa
def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON vars bloque
            | PROGRAM ID SEMICOLON bloque
    '''
    p[0] = "PROGRAM COMPILED SUCCESFULLY."


# Vars
def p_vars(p):
    '''
    vars : VARS varArgs
    '''

def p_varArgs(p):
    '''
    varArgs : ID COLON tipo SEMICOLON
        | ID COLON tipo COLON varArgs
        | ID COMMA varArgs
    '''

# Var tipo
def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''

# Bloque
def p_bloque(p):
    '''
    bloque : LBRACE estatutos RBRACE
    '''

# Estatutos
def p_estatutos(p):
    '''
    estatutos : estatuto
            | estatuto estatutos
            | empty
    '''

# Estatuto
def p_estatuto(p):
    '''
    estatuto : asignacion
            | condicion
            | escritura
    '''

# Asignacion
def p_asignacion(p):
    '''
    asignacion : ID EQUAL expresion SEMICOLON
    '''

# Expresion
def p_expresion(p):
    '''
    expresion : exp expresionP
    '''
def p_expresionP(p):
    '''
    expresionP : LESS exp
            | GREATER exp
            | DIFFERENT exp
            | empty
    '''

# Exp
def p_exp(p):
    '''
    exp : termino expP
    '''

def p_expP(p):
    '''
    expP : PLUS termino expP
            | MINUS termino expP
            | empty
    '''

# Término
def p_termino(p):
    '''
    termino : factor terminoP
    '''

def p_terminoP(p):
    '''
    terminoP : MULT factor terminoP
            | DIV factor terminoP
            | empty
    '''

# Escritura
def p_escritura(p):
    '''
    escritura : PRINT LPAREN escrituraP RPAREN SEMICOLON
    '''

def p_escrituraP(p):
    '''
    escrituraP : expresion
            | expresion COMMA escrituraP
            | CTES
            | CTES COMMA escrituraP
    '''

# Condicion
def p_condicion(p):
    '''
    condicion : condicionP bloque SEMICOLON
            | condicionP bloque ELSE bloque SEMICOLON
    '''

def p_condicionP(p):
    '''
    condicionP : IF LPAREN expresion RPAREN
    '''

# Factor
def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
            | factorP
    '''

def p_factorP(p):
    '''
    factorP : PLUS varcte
            | MINUS varcte
            | varcte
    '''

# VARCTE
def p_varcte(p):
    '''
    varcte : ID
            | CTEI
            | CTEF
    '''

def p_empty(p):
    '''
    empty :
    '''

# Error rule for syntax errors
def p_error(p):
   print("ERROR {}".format(p))

# Build the parser
yacc.yacc()

if __name__ == '__main__':
    try:
        arch_name = 'prueba2.txt'
        arch = open(arch_name,'r')
        print("Nombre de archivo a leer: " + arch_name)
        info = arch.read()
        # print(info)
        arch.close()
        if(yacc.parse(info, tracking = True) == 'PROGRAM COMPILED SUCCESFULLY.'):
            print("Correct syntax.")
        else:
            print("Syntax error.")
    except EOFError:
        print(EOFError)