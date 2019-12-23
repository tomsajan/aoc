import copy


class Intcode:
    def __init__(self, data):
        self.init_code = list(map(int, data.split(',')))
        self.code = []
        self.pos = 0
        self.input = []
        self.output = []
        self.wait = False
        self.current_code = None

        self.reset()

    def set_input(self, input):
        assert isinstance(input, int), 'not an int'
        assert len(self.input) <= 1, 'input len'
        self.input.append(input)
        # print(f'add input {input}, len {len(self.input)}')

    def set_output(self, output):
        assert isinstance(output, int), 'output not an int'
        self.output.append(output)
        # print(f'output {output}, len {len(self.output)}')

    def pop_input(self):
        if len(self.input) == 0:
            self.wait = True
            # print('no inputs, waiting')
            return
        return self.input.pop(0)

    def get_last_output(self):
        return self.output[-1]

    def set_noun(self, noun):
        self.code[1] = noun

    def set_verb(self, verb):
        self.code[2] = verb

    def reset(self):
        self.code = copy.deepcopy(self.init_code)
        self.pos = 0
        self.input = []
        self.output = []
        self.wait = False
        self.current_code = None

    def interpret_param(self, param, mode):
        mode = mode[-param] if len(mode) >= param else '0'
        if mode == '0':
            return self.code[self.pos + param]
        if mode == '1':
            return self.pos + param

    def _do_1(self, mode):
        par1 = self.interpret_param(1, mode)
        par2 = self.interpret_param(2, mode)
        par3 = self.interpret_param(3, mode)

        self.code[par3] = self.code[par1] + self.code[par2]
        assert self.code[par3] is not None, 'code None'
        self.pos += 4

    def _do_2(self, mode):
        par1 = self.interpret_param(1, mode)
        par2 = self.interpret_param(2, mode)
        par3 = self.interpret_param(3, mode)

        self.code[par3] = self.code[par1] * self.code[par2]
        assert self.code[par3] is not None, 'code None'
        self.pos += 4

    def _do_3(self, mode):
        par1 = self.interpret_param(1, mode)
        input_value = self.pop_input()
        if input_value is None:
            return
        self.code[par1] = input_value
        assert self.code[par1] is not None, 'code None'
        self.pos += 2

    def _do_4(self, mode):
        par1 = self.interpret_param(1, mode)
        self.set_output(self.code[par1])
        self.pos += 2
        # print('Output', self.output)

    def _do_5(self, mode):
        par1 = self.interpret_param(1, mode)
        par2 = self.interpret_param(2, mode)

        if self.code[par1] != 0:
            self.pos = self.code[par2]
        else:
            self.pos += 3

    def _do_6(self, mode):
        par1 = self.interpret_param(1, mode)
        par2 = self.interpret_param(2, mode)

        if self.code[par1] == 0:
            self.pos = self.code[par2]
        else:
            self.pos += 3

    def _do_7(self, mode):
        par1 = self.interpret_param(1, mode)
        par2 = self.interpret_param(2, mode)
        par3 = self.interpret_param(3, mode)

        if self.code[par1] < self.code[par2]:
            self.code[par3] = 1
        else:
            self.code[par3] = 0

        self.pos += 4

    def _do_8(self, mode):
        par1 = self.interpret_param(1, mode)
        par2 = self.interpret_param(2, mode)
        par3 = self.interpret_param(3, mode)

        if self.code[par1] == self.code[par2]:
            self.code[par3] = 1
        else:
            self.code[par3] = 0
        self.pos += 4

    def _do_99(self, mode):
        self.wait = True
        print('Exit', self.code[0])
        # submit(ic.output)
        # sys.exit(0)

    @staticmethod
    def parse_opcode(code):
        code = str(code)
        mode = code[:-2]
        op = code[-2:]
        return mode, int(op)

    def run(self):
        self.wait = False
        while not self.wait:
            opcode = self.code[self.pos]
            mode, op = self.parse_opcode(opcode)
            self.current_code = op

            func = getattr(self, f'_do_{op}')
            func(mode)
