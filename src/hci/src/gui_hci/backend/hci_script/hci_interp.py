import sys
import time
import logging
from PySide6.QtCore import Signal, QObject
from max_ble_hci import BleHci
from max_ble_hci.hci_packets import CommandPacket
from .cmd_structs import CMD_OPCODE, CMD_PARAM_LEN

class KillEvent:
    def __init__(self):
        self.killSet = False
    
    def set(self):
        self.killSet = True

    def unset(self):
        self.killSet = False

    def is_set(self):
        return self.killSet

class HciInterpreter(QObject):
    finished = Signal(int)

    def __init__(self, prog: str, logger_name: logging.Logger):
        super().__init__()
        self.prog = prog
        self.logger = logging.getLogger(logger_name)
        self.logger_name = logger_name
        self.vars = None
        self.devs = None
        self.loops = None
        self.loopends = None
        self.error = None
        self.pc = None
        self.stat = None
        self.kill_evt = KillEvent()

        self.ops = {
            'FOR': self._for_loop,
            'IF': lambda x: self._if_block(x[0]),
            'ELSEIF': lambda x: self._if_block(x[0]),
            'ELSE': lambda x: x,
            'WHILE': lambda x: self._while_loop(x[0]),
            'DEVADD': self._add_device,
            'CMD': self._command,
            'WAIT': self._wait,
            'ASSIGN': self._assign,
            'PRINT': self._print,
            'BOOLOP': self._bool_op,
            'RELOP': self._relative_op,
            'BINOP': self._binary_op,
            'BITOP': self._bitwise_op,
            'NUM' : lambda x: x[0],
            'STR' : lambda x: x[0],
            'BOOL' : lambda x: x[0],
            'VAR' : lambda x: self.vars.get(x[0]),
            'GROUP' : lambda x: self._grouping_op(x[0]),
            'UNARY' : self._unary_op,
        }

        self.rel_ops = {
            '<' : lambda lhs, rhs: lhs < rhs,
            '<=' : lambda lhs, rhs: lhs <= rhs,
            '>' : lambda lhs, rhs: lhs > rhs,
            '>=' : lambda lhs, rhs: lhs >= rhs,
            '==' : lambda lhs, rhs: lhs == rhs,
            '!=' : lambda lhs, rhs: lhs != rhs
        }

        self.bin_ops = {
            '+' : lambda lhs, rhs: lhs + rhs,
            '-' : lambda lhs, rhs: lhs - rhs,
            '*' : lambda lhs, rhs: lhs * rhs,
            '/' : lambda lhs, rhs: lhs / rhs,
            '%' : lambda lhs, rhs: lhs % rhs,
            '**' : lambda lhs, rhs: lhs ** rhs
        }

        self.bit_ops = {
            '|' : lambda lhs, rhs: int(lhs) | int(rhs),
            '&' : lambda lhs, rhs: int(lhs) & int(rhs),
            '~' : lambda rhs: self._invert(int(rhs)),
            '^' : lambda lhs, rhs: int(lhs) ^ int(rhs),
            '<<' : lambda lhs, rhs: int(lhs) << int(rhs),
            '>>' : lambda lhs, rhs: int(lhs) >> int(rhs)
        }

    def __del__(self):
        try:
            for devName, dev in self.devs.items():
                dev.exit()
        except NameError:
            pass

    def set_prog(self, prog):
        self.prog = prog

    def run(self):
        self.vars = {}
        self.devs = {}
        self.start_loops = []
        self.end_loops = {}
        self.start_ifblocks = []
        self.ifblock_elseifs = {}
        self.ifblock_elses = {}
        self.end_ifblocks = {}
        
        self.error = False
        self.pc = 0

        self.stat = list(self.prog)
        self.stat.sort()

        self.error = self._check_blocks()
        self._parse_ifs()

        if self.error:
            raise SyntaxError('Missing block end bracket.')

        while not self.kill_evt.is_set():
            if self.pc >= len(self.stat):
                break

            lineno = self.stat[self.pc]
            dev, instr = self.prog[lineno]
            op = instr[0]
            params = instr[1:]
            if len(params) == 1: params = params[0]

            if op == 'CMD' and dev is not None:
                retval = self.ops[op](params, dev=dev)
                if retval == -1:
                    for devName, dev in self.devs.items():
                        dev.exit()
                        self.logger.user("Closing device: %s", devName)
                    self.finished.emit(-1)
                    return
                self.pc += 1
                continue

            if op != 'LVL': retval = self.ops[op](params)
            if retval == -1:
                for devName, dev in self.devs.items():
                    dev.exit()
                    self.logger.user("Closing device: %s", devName)
                self.finished.emit(-1)
                return
            
            self.pc += 1
        
        for devName, dev in self.devs.items():
            dev.exit()
            self.logger.user("Closing device: %s", devName)
        if self.kill_evt.is_set():
            self.finished.emit(-2)
        else:
            self.finished.emit(0)

    def _add_device(self, params):
        dev_name = params[0]
        port_id = params[1]

        if isinstance(dev_name, tuple):
            dev_name = self.ops[dev_name[0]](dev_name[1:])
        if isinstance(port_id, tuple):
            port_id = self.ops[port_id[0]](port_id[1:])

        self.devs[dev_name] = BleHci(port_id, logger_name=self.logger_name)

    def _parse_ifs(self):
        if_starts = []
        curr_ifs = 0
        for idx in range(len(self.stat)):
            lineno = self.stat[idx]
            if 'ELSEIF' in self.prog[lineno][1]:
                if self.ifblock_elseifs.get(if_starts[-curr_ifs]) is not None:
                    self.ifblock_elseifs[if_starts[-curr_ifs]].append(lineno)
                    continue
                self.ifblock_elseifs[if_starts[-curr_ifs]] = [lineno]
                continue
            if 'ELSE' in self.prog[lineno][1]:
                self.ifblock_elses[if_starts[-curr_ifs]] = lineno
                continue
            if '}' in self.prog[lineno][1] or ('LVL', '}') in self.prog[lineno][1]:
                if self.end_loops:
                    if lineno in self.end_loops.values():
                        continue
                if idx < len(self.stat) - 1:
                    if 'ELSE' in self.prog[self.stat[idx+1]][1]:
                        continue
                    if 'ELSEIF' in self.prog[self.stat[idx+1]][1]:
                        continue
                self.end_ifblocks[if_starts.pop()] = lineno
                curr_ifs -= 1

            if self.prog[lineno][1][0] == 'IF':
                if_starts.append(lineno)
                self.start_ifblocks.append(lineno)
                curr_ifs += 1

    def _check_blocks(self):
        block_starts = []
        for lineno in self.stat:
            if '}' in self.prog[lineno][1] or ('LVL', '}') in self.prog[lineno][1]:
                key = block_starts.pop()
                if key in self.start_loops:
                    self.end_loops[key] = lineno
            if self.prog[lineno][1][0] in ['FOR', 'WHILE']:
                block_starts.append(lineno)
                self.start_loops.append(lineno)
            if self.prog[lineno][1][0] in ['IF', 'ELSEIF', 'ELSE']:
                block_starts.append(lineno)

        return len(block_starts) > 0

    def _invert(self, num: int):
        num_size = max((num.bit_length() + 7) // 8, 1)
        inv_factor = int('FF'*num_size, 16)

        return num^inv_factor

    def _for_loop(self, params):
        loop_key = params[0]
        loop_start = params[1]
        loop_stop = params[2]
        loop_step = params[3]

        if isinstance(loop_start, tuple):
            loop_start = self.ops[loop_start[0]](loop_start[1:])
        if isinstance(loop_stop, tuple):
            loop_stop = self.ops[loop_stop[0]](loop_stop[1:])
        if loop_step is None:
            loop_step = 1
        elif isinstance(loop_step, tuple):
            loop_step = self.ops[loop_step[0]](loop_step[1:])

        self.vars[loop_key] = loop_start
        loop_startpc = self.pc + 1
        loop_endline = self.end_loops[self.stat[self.pc]]
        while self.vars[loop_key] < loop_stop and not self.kill_evt.is_set():
            self.pc = loop_startpc
            while True and not self.kill_evt.is_set():
                lineno = self.stat[self.pc]
                if lineno == loop_endline:
                    break

                dev, instr = self.prog[lineno]
                op = instr[0]
                params = instr[1:]

                if len(params) == 1: params = params[0]
                if op == 'CMD' and dev is not None:
                    retval = self.ops[op](params, dev=dev)
                if op != 'LVL': retval = self.ops[op](params)
                if retval == -1: return -1

                self.pc += 1
            self.vars[loop_key] += loop_step

        self.pc = self.pc - 1
    
    def _if_block(self, params):
        op = params[0]
        passes = self.ops[op](params[1:])
        if_start = self.stat[self.pc]

        for key, val in self.ifblock_elseifs.items():
            if if_start in val:
                if_start = key

        if passes:
            self.pc = self.pc + 1
            if_end = self.ifblock_elseifs.get(if_start)
            if if_end is not None:
                for endline in if_end:
                    if endline <= self.stat[self.pc]:
                        continue
                    if_end = endline
                    break
            if if_end is None or isinstance(if_end, list):
                if_end = self.ifblock_elses.get(if_start, self.end_ifblocks[if_start])
            while self.stat[self.pc] < if_end and not self.kill_evt():
                lineno = self.stat[self.pc]
                dev, instr = self.prog[lineno]
                op = instr[0]
                params = instr[1:]

                if len(params) == 1:
                    params = params[0]
                if op == 'CMD' and dev is not None:
                    retval = self.ops[op](params, dev=dev)
                if op != 'LVL':
                    retval = self.ops[op](params)
                if retval == -1: return -1
                self.pc += 1

            self.pc = self.stat.index(self.end_ifblocks.get(if_start)) - 1
            return
        
        if_end = self.ifblock_elseifs.get(if_start)
        if if_end is not None:
            for endline in if_end:
                if endline <= self.stat[self.pc]:
                    continue
                if_end = endline
                break
        if if_end is None or isinstance(if_end, list):
            if_end = self.ifblock_elses.get(if_start, self.end_ifblocks[if_start])

        self.pc = self.stat.index(if_end) - 1
    
    def _while_loop(self, params):
        loop_startpc = self.pc + 1
        loop_endline = self.end_loops[self.stat[self.pc]]
        loop_cond = params

        while True and not self.kill_evt.is_set():
            passes = self.ops[loop_cond[0]](loop_cond[1:])
            if not passes:
                break
            self.pc = loop_startpc
            while True and not self.kill_evt.is_set():
                lineno = self.stat[self.pc]
                if lineno == loop_endline:
                    break

                dev, instr = self.prog[lineno]
                op = instr[0]
                params = instr[1:]

                if len(params) == 1: params = params[0]
                if op == 'CMD' and dev is not None:
                    retval = self.ops[op](params, dev=dev)
                if op != 'LVL': retval = self.ops[op](params)
                if retval == -1: return -1

                self.pc += 1
            
        self.pc = loop_endline - 1
            
    def _command(self, params, dev=None):
        cmd = params[0]
        cmd_params = []
        return_id = params[2]
        if isinstance(cmd, tuple):
            cmd = self.ops[cmd[0]](cmd[1])

        if params[1] is not None:
            eval_params = self._evaluate_params(params[1])
            param_lens = self._get_param_lens(eval_params, cmd)
            for idx, param in enumerate(eval_params):
                cmd_params.extend(self._to_le_nbyte_list(param, param_lens[idx]))

        ogf, ocf = CMD_OPCODE[cmd]

        cmd_pkt = CommandPacket(ogf, ocf, params=cmd_params)
        if dev:
            retval = self.devs[dev].write_command(cmd_pkt)
        elif self.devs:
            dev = next(iter(self.devs.values()))
            retval = dev.write_command(cmd_pkt)
        else:
            self.logger.error("An HCI connection must be established before sending commands.")
            return -1
        retval = 0
        if return_id is not None:
            self.vars[return_id] = retval

    def _wait(self, params):
        if isinstance(params, tuple):
            sleep_time = self.ops[params[0]](params[1:])
        else:
            sleep_time = params

        time.sleep(sleep_time)
    
    def _assign(self, params):
        key = params[0]
        val = params[1]
        self.vars[key] = self.ops[val[0]](val[1:])
    
    def _print(self, params):
        if isinstance(params, tuple):
            print_data = self.ops[params[0]](params[1:])
        else:
            print_data = params
        self.logger.print(print_data)
    
    def _bool_op(self, params):
        if params[1] is None and params[2] is None:
            expr = params[0]
            if isinstance(expr, tuple):
                return self.ops[expr[0]](expr[1:])
            if isinstance(expr, bool):
                return expr
            self.logger.error("Well that's an issue.")
            return -1

        if params[2] is None:
            expr = params[1]
            if isinstance(expr, tuple):
                return not self.ops[expr[0]](expr[1:])
            if isinstance(expr, bool):
                return not expr
            self.logger.error("Woah, there's that issue again.")
            return -1
        
        lhs = params[0]
        op = params[1]
        rhs = params[2]

        if isinstance(lhs, tuple):
            lhs = self.ops[lhs[0]](lhs[1:])
        
        if isinstance(rhs, tuple):
            rhs = self.ops[rhs[0]](rhs[1:])

        if op in ['||', 'OR', 'or']:
            return lhs or rhs
        
        if op in ['&&', 'AND', 'and']:
            return lhs and rhs

        self.logger.error("There's no other operators, what are you doing?")
        return -1

    def _relative_op(self, params):
        lhs = params[0]    
        op = params[1]
        rhs = params[2]

        if isinstance(lhs, tuple):
            lhs = self.ops[lhs[0]](lhs[1:])

        if isinstance(rhs, tuple):
            rhs = self.ops[rhs[0]](rhs[1:])

        return self.rel_ops[op](lhs, rhs)
        
    def _binary_op(self, params):
        lhs = params[0]
        op = params[1]
        rhs = params[2]

        if isinstance(lhs, tuple):
            lhs = self.ops[lhs[0]](lhs[1:])

        if isinstance(rhs, tuple):
            rhs = self.ops[rhs[0]](rhs[1:])

        return self.bin_ops[op](lhs, rhs)
    
    def _bitwise_op(self, params):
        lhs = params[0]
        op = params[1]
        rhs = params[2]

        if isinstance(lhs, tuple):
            lhs = self.ops[lhs[0]](lhs[1:])
        
        if isinstance(rhs, tuple):
            rhs = self.ops[rhs[0]](rhs[1:])

        if lhs is not None:
            return self.bit_ops[op](lhs, rhs)
        
        return self.bit_ops[op](rhs)
        
    def _unary_op(self, params):
        rhs = params[1]

        if isinstance(rhs, tuple):
            rhs = self.ops[rhs[0]](rhs[1:])

        return -rhs
    
    def _grouping_op(self, params):
        if isinstance(params, tuple):
            return self.ops[params[0]](params[1:])
        return params
    
    def _evaluate_params(self, params):
        eval_params = []
        for param in params:
            if isinstance(param, tuple):
                eval_params.append(self.ops[param[0]](param[1:]))
            else:
                eval_params.append(param)

        return eval_params

    def _get_param_lens(self, params, cmd):
        param_lens = []
        in_loop = False
        num_loop = 0
        loop_idx = 0
        loop_vals = []
        for idx, param in enumerate(params):
            if in_loop:
                if num_loop == 0:
                    in_loop = False
                    continue
                lidx = (idx - loop_idx) % len(loop_vals)
                param_lens.append(loop_vals[lidx])
                num_loop -= 1
                continue

            if isinstance(CMD_PARAM_LEN[cmd][idx], list):
                loop_idx = idx
                if CMD_PARAM_LEN[cmd][idx][0] > 0:
                    num_loop = params[CMD_PARAM_LEN[cmd][idx][0]]*(len(CMD_PARAM_LEN[cmd][idx])-1)
                else:
                    if params[abs(CMD_PARAM_LEN[cmd][idx][0])] in [1, 2, 4]:
                        num_loop = len(CMD_PARAM_LEN[cmd][idx]) - 1
                    elif params[abs(CMD_PARAM_LEN[cmd][idx][0])] in [3, 5, 6]:
                        num_loop = 2*(len(CMD_PARAM_LEN[cmd][idx]) - 1)
                    else:
                        num_loop = 3*(len(CMD_PARAM_LEN[cmd][idx]) - 1)
                loop_vals = CMD_PARAM_LEN[cmd][idx][1:]
                in_loop = True
                param_lens.append(loop_vals[0])
                num_loop -= 1
            elif CMD_PARAM_LEN[cmd][idx] < 0:
                param_lens.append(params[abs(CMD_PARAM_LEN[cmd][idx])-1])
            else:
                param_lens.append(CMD_PARAM_LEN[cmd][idx])

        return param_lens

    def _to_le_nbyte_list(self, value, n_bytes):
        little_endian = []
        for i in range(n_bytes):
            num_masked = (value & (0xFF << 8 * i)) >> (8 * i)
            little_endian.append(num_masked)
        return little_endian