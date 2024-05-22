import ply.yacc as yacc
import hci_lex

tokens = hci_lex.tokens

precedence = (
    ("left", "PLUS", "MINUS", "AND", "OR", "BITWISELS", "BITWISERS"),
    ("left", "MUL", "DIV", "MOD", "BITWISEAND", "BITWISEOR", "BITWISEXOR"),
    ("left", "POWER", "BITWISENOT"),
    ("right", "UMINUS", "NOT"),
)

linecount = -100


def p_program(p):
    """program : program statement
    | statement"""
    if len(p) == 2 and p[1]:
        p[0] = {}
        line, stat = p[1]
        p[0][line] = stat
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = {}
        if p[2]:
            line, stat = p[2]
            p[0][line] = stat


def p_statement(p):
    """statement : command NEWLINE
    | DEV command NEWLINE"""
    global linecount
    if linecount < 0:
        linecount = p.lineno(-1)
    if len(p) == 3:
        if isinstance(p[1], str):
            print(f"{p[1]} at line {linecount}")
            p[0] = None
            p.parser.error += 1
        p[0] = (linecount, (None, p[1]))
    else:
        if isinstance(p[2], str):
            print(f"{p[2]} at line {linecount}")
            p[0] = None
            p.parser.error += 1
        p[0] = (linecount, (p[1], p[2]))

    linecount += 1


def p_statement_newline(p):
    """statement : NEWLINE"""
    global linecount
    p[0] = None
    linecount += 1


def p_statement_bad(p):
    """statement : error NEWLINE"""
    global linecount
    print(f"Malformed statment at line {linecount}.")
    p[0] = None
    p.parser.error += 1
    linecount += 1


def p_command_for(p):
    """command : FOR ID ASSIGN expr TO expr optstep optlvlinc"""
    p[0] = ("FOR", p[2], p[4], p[6], p[7], p[8])


def p_command_for_bad_initial(p):
    """command : FOR ID ASSIGN error TO expr optstep optlvlinc"""
    p[0] = "Bad initial value in for statement"


def p_command_for_bad_final(p):
    """command : FOR ID ASSIGN expr TO error optstep optlvlinc"""
    p[0] = "Bad final value in for statement"


def p_command_for_bad_step(p):
    """command : FOR ID ASSIGN expr TO expr STEP error"""
    p[0] = "Malformed step in for statement"


def p_command_if(p):
    """command : IF boolexpr optlvlinc
    | IF expr optlvlinc"""
    p[0] = ("IF", p[2], p[3])


def p_command_if_bad(p):
    """command : IF error optlvlinc"""
    p[0] = "Bad boolean expression"


def p_command_elseif(p):
    """command : optlvldec ELSE IF boolexpr optlvlinc"""
    p[0] = ("ELSEIF", p[4], p[1], p[5])


def p_command_elseif_bad(p):
    """command : optlvldec ELSE IF error optlvlinc"""
    p[0] = "Bad boolean expression"


def p_command_else(p):
    """command : optlvldec ELSE optlvlinc"""
    p[0] = ("ELSE", p[1], p[3])


def p_command_while(p):
    """command : WHILE boolexpr optlvlinc
    | WHILE bool optlvlinc"""
    p[0] = ("WHILE", p[2], p[3])


def p_command_while_bad(p):
    """command : WHILE error optlvlinc"""
    p[0] = "Bad boolean expression"


def p_command_devadd(p):
    """command : ADD_DEV ID expr"""
    p[0] = ("DEVADD", p[2], p[3])


def p_command_devadd_bad(p):
    """command : ADD_DEV ID error"""
    p[0] = "Bad expression in ADD_DEV"


def p_command_cmd(p):
    """command : CMD
    | CMD paramlist"""
    if len(p) == 2:
        p[0] = ("CMD", p[1], None)
    else:
        p[0] = ("CMD", p[1], p[2])


def p_command_cmd_bad(p):
    """command : CMD error"""
    p[0] = "Bad command parameters"


def p_command_wait(p):
    """command : WAIT expr"""
    p[0] = ("WAIT", p[2])


def p_command_wait_bad(p):
    """command : WAIT error"""
    p[0] = "Bad argument to WAIT"


def p_command_assignvar(p):
    """command : ID ASSIGN expr"""
    if len(p) == 5:
        p[0] = ("ASSIGN", p[2], p[4])
    else:
        p[0] = ("ASSIGN", p[1], p[3])


def p_command_assignvar_bad(p):
    """command : ID ASSIGN error"""
    p[0] = "Bad expression for variable assignment"


def p_command_lvlchange(p):
    """command : STEPIN
    | STEPOUT"""
    p[0] = ("LVL", p[1])


def p_command_print(p):
    """command : PRINT expr"""
    p[0] = ("PRINT", p[2])


def p_optstep(p):
    """optstep : STEP expr
    | empty"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None


def p_optlvlinc(p):
    """optlvlinc : STEPIN
    | empty"""
    if len(p) == 2:
        p[0] = ("LVL", p[1])
    else:
        p[0] = None


def p_optlvldec(p):
    """optlvldec : STEPOUT
    | empty"""
    if len(p) == 2:
        p[0] = ("LVL", p[1])
    else:
        p[0] = None


def p_boolexpr(p):
    """boolexpr : relexpr
    | boolexpr AND boolexpr
    | boolexpr OR boolexpr
    | NOT boolexpr"""
    if len(p) == 2:
        p[0] = ("BOOLOP", p[1], None, None)
    elif len(p) == 3:
        p[0] = ("BOOLOP", p[1], p[2], None)
    else:
        p[0] = ("BOOLOP", p[1], p[2], p[3])


def p_relexpr(p):
    """relexpr : expr LT expr
    | expr LTE expr
    | expr GT expr
    | expr GTE expr
    | expr EQUAL expr
    | expr NOTEQUAL expr"""
    p[0] = ("RELOP", p[1], p[2], p[3])


def p_expr_binary(p):
    """expr : expr PLUS expr
    | expr MINUS expr
    | expr MUL expr
    | expr DIV expr
    | expr MOD expr
    | expr POWER expr"""
    p[0] = ("BINOP", p[1], p[2], p[3])


def p_expr_bitwise(p):
    """expr : expr BITWISEAND expr
    | expr BITWISEOR expr
    | expr BITWISEXOR expr
    | expr BITWISELS INT
    | expr BITWISERS INT
    | BITWISENOT expr"""
    if len(p) == 3:
        p[0] = ("BITOP", None, p[1], p[2])
    else:
        p[0] = ("BITOP", p[1], p[2], p[3])


def p_expr_number(p):
    """expr : INT
    | FLOAT"""
    p[0] = ("NUM", p[1])


def p_expr_string(p):
    """expr : STR"""
    p[0] = ("STR", p[1])


def p_expr_variable(p):
    """expr : ID"""
    p[0] = ("VAR", p[1])


def p_expr_bool(p):
    """expr : bool"""
    p[0] = ("BOOL", p[1])


def p_expr_group(p):
    """expr : LPAREN expr RPAREN"""
    p[0] = ("GROUP", p[2])


def p_expr_unary(p):
    """expr : MINUS expr %prec UMINUS"""
    p[0] = ("UNARY", "-", p[2])


def p_bool(p):
    """bool : TRUE
    | FALSE"""
    p[0] = ("BOOL", p[1] == "TRUE")


def p_paramlist(p):
    """paramlist : paramlist SEP param
    | param"""
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]


def p_param_expr(p):
    """param : expr
    | boolexpr"""
    p[0] = p[1]


def p_empty(p):
    """empty :"""


def p_error(p):
    if not p:
        print("Syntax error at EOF")


parser = yacc.yacc()


def parse(data, debug=0):
    parser.error = 0
    prog = parser.parse(data, debug=debug)
    if parser.error:
        print("Errors present in script")
    return prog
