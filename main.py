
tokens = ['NUMERO','MAIS','MENOS','VEZES','DIVIDE','EPAREN','DPAREN','RECEBE','IGUAL','MAIOR','MENOR','MAIORIGUAL','MENORIGUAL','DIFERENTE','PONTOVIRG','VIRGULA','ECOLCHETE','DCOLCHETE','ECHAVE','DCHAVE','ABRECOMENT','FECHACOMENT','ID']


t_MAIOR=r'>'
t_MENOR=r'<'
t_MAIORIGUAL=r'>='
t_MENORIGUAL=r'<='
t_DIFERENTE = r'!='
t_PONTOVIRG = r';'
t_VIRGULA = r','
t_DCOLCHETE = r'\['
t_ECOLCHETE = r'\]'
t_ECHAVE=r'\{'
t_DCHAVE=r'\}'
t_ignore_ABRECOMENT=r'\\\*' # Ignora
t_ignore_FECHACOMENT=r'\*\\'# Ignora
t_IGUAL = r'=='
t_RECEBE = r'='
t_MAIS = r'\+'
t_MENOS = r'-'
t_VEZES = r'\*'
t_DIVIDE = r'/'
t_EPAREN = r'\('
t_DPAREN = r'\)'

reservado = {
    'if':'IF',
    'else':'ELSE',
    'int':'INT',
    'return':'RETURN',
    'void':'VOID',
    'while':'WHILE'
}
tokens = tokens + list(reservado.values())


def t_NUMERO(t):
    r'\d+' #um ou mais inteiros
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservado.get(t.value,'ID')
    return t

t_ignore = ' \t'

def t_error(t):
    print("Caracter Inválido '%s'"% t.value[0])
    t.lexer.skip(1)

def test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


import ply.lex as lex
lexer = lex.lex()

vars = {}

precedence = (
    ('left','MAIS','MENOS'),
    ('left','VEZES','DIVIDE'),
    ('right','MENOS'),
    )

def p_program_declaration_list (p):
    'program : declaration-list'
    # p[0] = p[1]
def p_declaration_list_declaration_list_declaration(p):
    'declaration-list : declaration-list declaration'
    # p[0] = p[2] ## Como que retorna dois valores??

def p_declaration_list_declaration(p):
    'declaration-list : declaration'
    # p[0] = p[1]

def p_declaration_var_declaration(p):
    'declaration : var-declaration'
    # p[0] =p[1]

def p_declaration_fun_declaration(p):
    'declaration : fun-declaration'
    # p[0] = p[1]

def p_var_declaration_type_specifier_ID(p):
    'var-declaration : type-specifier ID PONTOVIRG'
    # vars[p[2]] = 0

def p_var_desclaration_type_specifier_ID_vet(p):
    'var-declaration : type-specifier ID ECOLCHETE NUMERO DCOLCHETE PONTOVIRG' 
    # vars[p[2]] = [x for x in range(0,p[4])]

def p_type_specifier_int(p):
    'type-specifier : INT'
    # p[0] = p[1]

def p_type_specifier_void(p):
    'type-specifier : VOID'
    # p[0] = p[1]

def p_fun_declaration_type_specifier_id(p):
    'fun-declaration : type-specifier ID DPAREN params EPAREN compound-stmt'
    # p[0] = (p[1])

def p_params(p):
    'params : params-list'
    # p[0]=p[1]

def p_params_void(p):
    'params : VOID'
    # p[0]=p[1]

def p_params_list(p):
    'params-list : params-list VIRGULA param'
    # p[0]= (p[1],p[2],p[3])

def p_params_list_params(p):
    'params-list : param'
    # p[0]= p[1]

def p_param(p):
    'param : type-specifier ID'
    # p[0]=p[2]

def p_param_1(p):
    'param : type-specifier ID DCOLCHETE ECOLCHETE'
    # p[0]=p[2]

#daqui
def p_compound_stmt(p):
    'compound-stmt :  ECHAVE local-declarations statement-list DCHAVE'
    # p[0]=p[2]

def p_local_declarations(p):
    'local-declarations : local-declarations var-declaration'

def p_local_declarations_1(p):
    'local-declarations : empty'

def p_statement_list(p):
    'statement-list : statement-list statement'
    # p[0] = (p[1], p[2])

def p_statement_list_empty(p):
    'statement-list : empty'
    # p[0]=p[1]

def p_statement(p):
    'statement : expression-stmt'
    # p[0]=p[1]

def p_statement_1(p):
    'statement : compound-stmt'
    # p[0]=p[1]

def p_statement_2(p):
    'statement : selection-stmt'
    # p[0]=p[1]

def p_statement_3(p):
    'statement : iteration-stmt'
    # p[0]=p[1]

def p_statement_4(p):
    'statement : return-stmt'
    # p[0]=p[1]

def p_expession_stmt(p):
    'expression-stmt : expression PONTOVIRG'

def p_expession_stmt_1(p):
    'expression-stmt : PONTOVIRG'

def p_selection_stmt(p):
    'selection-stmt : IF EPAREN expression DPAREN statement'

def p_selection_stmt_1(p):
    'selection-stmt : IF EPAREN expression DPAREN statement ELSE statement'

def p_iteration_stmt(p):
    'iteration-stmt : WHILE EPAREN expression DPAREN statement'

def p_return_stmt(p):
    'return-stmt : RETURN PONTOVIRG'

def p_return_stmt_1(p):
    'return-stmt : RETURN expression PONTOVIRG'

def p_expression(p):
    'expression : var RECEBE expression PONTOVIRG'

def p_expression_1(p):
    'expression : simple-expression'

def p_var(p):
    'var : ID'

def p_var_1(p):
    'var : ID DCOLCHETE expression ECOLCHETE'

def p_simple_expression(p):
    'simple-expression : additive-expression relop additive-expression'

def p_simple_expression_1(p):
    'simple-expression : additive-expression'

def p_relop(p):
    'relop : MAIOR'

def p_relop_1(p):
    'relop : MENOR'

def p_relop_2(p):
    'relop : IGUAL'

def p_relop_3(p):
    'relop : MAIORIGUAL'

def p_relop_4(p):
    'relop : MENORIGUAL'

def p_relop_5(p):
    'relop : DIFERENTE'

def p_additive_expression(p):
    'additive-expression : additive-expression addop term'

def p_additive_expression_1(p):
    'additive-expression : term'

def p_addop(p):
    'addop : MAIS'

def p_addop_1(p):
    'addop : MENOS'

def p_term(p):
    'term : term mulop factor'

def p_term_1(p):
    'term : factor'

def p_mulop(p):
    'mulop : VEZES'
def p_mulop_1(p):
    'mulop : DIVIDE'
def p_factor(p):
    'factor : EPAREN expression DPAREN'
def p_factor_1(p):
    'factor : var'
def p_factor_2(p):
    'factor : call'
def p_factor_3(p):
    'factor : NUMERO'

def p_call(p):
    'call : ID DPAREN args EPAREN'

def p_args(p):
    'args : arg-list'
def p_args_1(p):
    'args : empty'
def p_arg_list(p):
    'arg-list : arg-list VIRGULA expression'

def p_arg_list_1(p):
    'arg-list : expression'

def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc
parser = yacc.yacc()


with open('test1','r') as f:
    x = f.readlines()
    #parser.parse(x)
    print(x)

# while True:
#     try:
#         s = input('calc > ') 
#     except EOFError:
#         break
#     parser.parse(s)