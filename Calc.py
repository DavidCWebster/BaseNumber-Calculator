from pickle import NONE
import ply.lex as lex
import ply.yacc as yacc
import basesMod

tokens= [
    "TESTNUM",
    "BASENUM",
    "INT",
    "FLOAT",
    "NAME",
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "EQUALS",
    "DIVIDE",
    "MODULUS"
]

t_PLUS= r'\+'
t_MINUS= r'\-'
t_MULTIPLY= r'\*'
t_EQUALS= r'\='
t_DIVIDE= r'/'
t_MODULUS= r'%'

t_ignore=r'\ '


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value=float(t.value)
    raise ValueError("Does not support decimals")

    return t

def t_BASENUM(t):
    #r'\[(\d+,)+\]'
    r'\d+\,\d+'
    
    t.value=basesMod.base(t.value.split(","),Pbase)
    return t

def t_TESTNUM(t):
    r'\[(\d+\,?)*]'
    t.value=basesMod.removeEdge(t.value)
    
    t.value=t.value.split(",")
    t.value=[int(x) for x in t.value]

    t.value=basesMod.base(t.value,Pbase)
    
    return t


def t_INT(t):
    r'\d+'
    t.value=basesMod.base(t.value,Pbase)


    return t



def t_Name(t):
    r'[a-zA-Z_][a-zA-z_0-9]*'
    t.type='NAME'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip

lexer= lex.lex()

precedence= (

    ('left', 'PLUS','MINUS'),
    ('left', 'MULTIPLY')

)

def p_calc(p):
    ''' 
    calc : expression
         | var_assign 
         | empty
     '''
    print(run(p[1]))

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
    '''
    p[0] = ('=', p[1], p[3])

def p_expression(p):
    '''
    expression : expression MULTIPLY expression
               | expression PLUS expression
               | expression MINUS expression
               | expression DIVIDE expression
               | expression MODULUS expression
    '''

    p[0]=(p[2], p[1], p[3])

def p_expression_int_float_BaseNum(p):
    '''
    expression : INT
               | FLOAT
               | BASENUM
               | TESTNUM
    '''
    p[0]=p[1]

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0]=('var', p[1])

def p_error(p):
    print("Syntax error")

def p_empty(p):
    '''
    empty :
    '''
    p[0]=None

parser=yacc.yacc()

env={}

def run(p):
    global env
    if type(p)==tuple:
        if p[0]=='+':
            return run(p[1])+run(p[2])
        elif p[0]=='-':
            return run(p[1])-run(p[2])
        elif p[0]=='*':
            return run(p[1])*run(p[2])
        elif p[0]=='/':
            return run(p[1])//run(p[2])
        elif p[0]=='%':
            return run(p[1])%run(p[2])
        elif p[0]=='=':
            env[p[1]]=run(p[2])
        elif p[0]=='var':
            if p[1] not in env:
                return 'undeclared variable found'
            else:
                return env[p[1]]

    else:
        return p





while True:
    

    try:
        Pbase=int(input("Please enter the base you would like to use: "))
    except ValueError:
        print("Please enter an integer")
        continue
        

    
    
    s=input('Enter Calculation: ')

    try:
        parser.parse(s)

    except EOFError:
        break
        
    
        

    







