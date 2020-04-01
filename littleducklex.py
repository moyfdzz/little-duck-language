# -----------------------------------------------------------------------------
# Moisés Fernández Zárate A01197049
# littleducklex.py
#
# Little Duck Language 2020 scanner with python using PLY (Python Lex Yacc).
# -----------------------------------------------------------------------------

import sys
import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'program' : 'PROGRAM',
    'print' : 'PRINT',
    'int' : 'INT',
    'float' : 'FLOAT',
    'vars' : 'VARS',
}

tokens = [
    'EQUAL',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'ID',
    'CTEI',
    'CTEF',
    'CTES',
    'LPAREN',
    'RPAREN',
    'DOT',
    'COMMA',
    'LBRACE',
    'RBRACE',
    'COLON',
    'SEMICOLON',
    'GREATER',
    'LESS',
    'DIFFERENT'
] + list(reserved.values())

t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = r'\,'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_GREATER = r'\>'
t_LESS = r'\<'
t_DIFFERENT = r'\<>'

# Ignore characters such as spaces and tabs
t_ignore  = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTES(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()