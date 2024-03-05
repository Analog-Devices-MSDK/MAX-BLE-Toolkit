import hci_lex
import hci_parse
from hci_interp import HciInterpreter
import hci_lex as hci_lex
import ply.lex as lex
import re
from cmd_structs import CMD_OPCODE, CMD_PARAM_LEN

# progfile = 'cmd_test.txt'
# progfile = 'loop_test.txt'
# progfile = 'boolop_test.txt'
# progfile = 'binop_test.txt'
# progfile = 'bitop_test.txt'
# progfile = 'func_test.txt'
# progfile = 'vars_test.txt'
# progfile = 'grouping_test.txt'
# progfile = 'ifblock_test.txt'
# progfile = 'loops_test.txt'
# progfile = 'command_test.txt'
# progfile = 'stress_test.txt'
progfile = 'simple_test.txt'

with open(progfile, 'r') as f:
    data = f.read()

if not data.endswith('\n'):
    data += '\n'

prog = hci_parse.parse(data, debug=1)
# for key, val in prog.items():
#     print(f'{key}: {val}')

interp = HciInterpreter(prog)
interp.run()
