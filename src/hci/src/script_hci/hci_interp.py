import sys
import time
from max_ble_hci import BleHci
from max_ble_hci.hci_packets import CommandPacket
from cmd_structs import CMD_OPCODE, CMD_PARAM_LEN

class HciInterpreter:
    def __init__(self, prog):
        self.prog = prog

        self.vars = None
        self.devs = None
        self.loops = None
        self.loopends = None
        self.error = None
        self.pc = None
        self.stat = None

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

        while True:
            if self.pc >= len(self.stat):
                break

            lineno = self.stat[self.pc]
            dev, instr = self.prog[lineno]
            op = instr[0]
            params = instr[1:]
            
            if len(params) == 1: params = params[0]

            if op == 'CMD' and dev is not None:
                self.ops[op](params, dev=dev)
                self.pc += 1
                continue

            if op != 'LVL': self.ops[op](params)
            
            self.pc += 1

    def _add_device(self, params):
        dev_name = params[0]
        port_id = params[1]

        if isinstance(dev_name, tuple):
            dev_name = self.ops[dev_name[0]](dev_name[1:])
        if isinstance(port_id, tuple):
            port_id = self.ops[port_id[0]](port_id[1:])

        self.devs[dev_name] = port_id
        # self.devs[dev_name] = BleHci(port_id)

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
        while self.vars[loop_key] < loop_stop:
            self.pc = loop_startpc
            while True:
                lineno = self.stat[self.pc]
                if lineno == loop_endline:
                    break

                dev, instr = self.prog[lineno]
                op = instr[0]
                params = instr[1:]

                if len(params) == 1: params = params[0]
                if op != 'LVL': self.ops[op](params)

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
            while self.stat[self.pc] < if_end:
                lineno = self.stat[self.pc]
                dev, instr = self.prog[lineno]
                op = instr[0]
                params = instr[1:]

                if len(params) == 1:
                    params = params[0]
                if op != 'LVL':
                    self.ops[op](params)

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

        while True:
            passes = self.ops[loop_cond[0]](loop_cond[1:])
            if not passes:
                break
            self.pc = loop_startpc
            while True:
                lineno = self.stat[self.pc]
                if lineno == loop_endline:
                    break

                dev, instr = self.prog[lineno]
                op = instr[0]
                params = instr[1:]

                if len(params) == 1: params = params[0]
                if op != 'LVL': self.ops[op](params)

                self.pc += 1
            
        self.pc = loop_endline - 1
            
    def _command(self, params, dev=None):
        cmd = params[0]
        cmd_params = []
        if isinstance(cmd, tuple):
            cmd = self.ops[cmd[0]](cmd[1:])

        if params[1] is not None:
            for idx, param in enumerate(params[1]):
                if isinstance(param, tuple):
                    param = self.ops[param[0]](param[1:])
                cmd_params.extend(self._to_le_nbyte_list(param, CMD_PARAM_LEN[cmd][idx]))

        ogf, ocf = CMD_OPCODE[cmd]

        cmd_pkt = CommandPacket(ogf, ocf, params=cmd_params)
        if dev:
            # self.devs[dev].write_command(cmd_pkt)
            print(f'{cmd} ({cmd_pkt.opcode}) -> {self.devs[dev]}')
        elif self.devs:
            dev = next(iter(self.devs.values()))
            # dev.write_command(cmd_pkt)
            print(f'{cmd} ({cmd_pkt.opcode}) -> {dev}')
        else:
            # raise RuntimeError(
            #     'An HCI connection must be established before commands can be sent.')
            print('An HCI connection must be established before commands can be sent.')
 
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

        print(print_data)
    
    def _bool_op(self, params):
        if params[1] is None and params[2] is None:
            expr = params[0]
            if isinstance(expr, tuple):
                return self.ops[expr[0]](expr[1:])
            if isinstance(expr, bool):
                return expr
            print("Well that's an issue")
            return None

        if params[2] is None:
            expr = params[1]
            if isinstance(expr, tuple):
                return not self.ops[expr[0]](expr[1:])
            if isinstance(expr, bool):
                return not expr
            print("Woah there's that issue again")
            return None
        
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
        
        print("There's no other operators, what you doing?")
        return None

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
    
    def _to_le_nbyte_list(self, value, n_bytes):
        little_endian = []
        for i in range(n_bytes):
            num_masked = (value & (0xFF << 8 * i)) >> (8 * i)
            little_endian.append(num_masked)
        return little_endian