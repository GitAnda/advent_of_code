class IntcodeProgram:
    opcode_length = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 99: 1}
    debug = False

    def __init__(self, initial_sequence):
        assert isinstance(initial_sequence, list) or isinstance(initial_sequence, tuple)
        self.sequence = list(initial_sequence)
        self.idx = 0
        self.count = 0
        self.opcode = self.get_opcode()
        self.parameter_modes = self.get_parameter_modes()
        self.relative_base = 0
        self.input = []
        self.output = []
        self.finished = False

    def __str__(self):
        for i in range(len(self.sequence)):
            print(self.sequence[i], end=' ')

    def add_input(self, new_input):
        if isinstance(new_input, int):
            self.input.append(new_input)
        elif isinstance(new_input, list):
            self.input = self.input + new_input
        elif isinstance(new_input, tuple):
            self.input = self.input + list(new_input)

    def get_parameter_value(self, mode, address):
        if mode == 0:
            return self.sequence[self.sequence[address]] if self.sequence[address] < len(self.sequence) else 0
        elif mode == 1:
            return self.sequence[address]
        elif mode == 2:
            return self.sequence[self.relative_base + self.sequence[address]] if self.relative_base + self.sequence[address] < len(self.sequence) else 0

    def get_opcode(self):
        opcode_immediate_mode = self.sequence[self.idx]
        if opcode_immediate_mode < 100:
            return opcode_immediate_mode
        else:
            return opcode_immediate_mode % 100

    def get_parameter_modes(self):
        opcode_immediate_mode = self.sequence[self.idx]
        if opcode_immediate_mode < 100:
            return [0]*(self.opcode_length[opcode_immediate_mode]-1)
        else:
            parameter_modes = [0]*(self.opcode_length[opcode_immediate_mode % 100] - len(str(opcode_immediate_mode)) + 1) + [int(x) for x in str(opcode_immediate_mode)[:-2]]
            return list(reversed(parameter_modes))

    def write_value_to_address(self, value, address, mode):
        if mode == 0:
            address = address
        elif mode == 1:
            print("Error: writing in immediate mode not supported")
            return

        elif mode == 2:
            address += self.relative_base

        if address > len(self.sequence) - 1:
            # print("Sequence extended to ", address, "addresses")
            self.sequence += [0]*(address-len(self.sequence)+1)
        self.sequence[address] = value
        if self.debug:
            print("Write", value, "to address", address)

    def run_opcode_1(self):
        first_number = self.get_parameter_value(self.parameter_modes[0], self.idx + 1)
        second_number = self.get_parameter_value(self.parameter_modes[1], self.idx + 2)

        if self.debug:
            print("Opcode 1:", first_number, "+", second_number, "=", first_number+second_number)
        self.write_value_to_address(first_number + second_number, self.sequence[self.idx + 3], self.parameter_modes[2])
        if self.debug: print()

        return True

    def run_opcode_2(self):
        first_number = self.get_parameter_value(self.parameter_modes[0], self.idx + 1)
        second_number = self.get_parameter_value(self.parameter_modes[1], self.idx + 2)

        if self.debug:
            print("Opcode 2:", first_number, "*", second_number, "=", first_number * second_number)
        self.write_value_to_address(first_number * second_number, self.sequence[self.idx + 3], self.parameter_modes[2])
        if self.debug: print()

        return True

    def run_opcode_3(self):
        if not self.input:
            self.input.append(int(input("Supply an integer: ")))

        if self.debug:
            print("Opcode 3: Input value is", self.input[0])

        self.write_value_to_address(self.input[0], self.sequence[self.idx + 1], self.parameter_modes[0])
        if self.debug: print()

        self.input.pop(0)

        return True

    def run_opcode_4(self):
        self.output.append(self.get_parameter_value(self.parameter_modes[0], self.idx + 1))
        # if self.output[-1] == ord('\n') and self.output[-2] == ord('\n'):
        #     print(' '+ ' '.join([chr(x) for x in self.output]), end='')
        #     self.output = []

        if self.debug:
            print("Opcode 4: Output value is", self.output[-1])
            print()

        return True

    def run_opcode_5(self):
        if self.debug:
            print("Opcode 5: Change index to", self.get_parameter_value(self.parameter_modes[1], self.idx + 2), "if", self.get_parameter_value(self.parameter_modes[0], self.idx + 1), "!= 0")
            print()

        if self.get_parameter_value(self.parameter_modes[0], self.idx + 1):
            self.idx = self.get_parameter_value(self.parameter_modes[1], self.idx + 2)
            return False
        return True

    def run_opcode_6(self):
        if self.debug:
            print("Opcode 6: Change index to", self.get_parameter_value(self.parameter_modes[1], self.idx + 2), "if", self.get_parameter_value(self.parameter_modes[0], self.idx + 1), "== 0")
            print()

        if self.get_parameter_value(self.parameter_modes[0], self.idx + 1) == 0:
            self.idx = self.get_parameter_value(self.parameter_modes[1], self.idx + 2)
            return False
        return True

    def run_opcode_7(self):
        first_number = self.get_parameter_value(self.parameter_modes[0], self.idx + 1)
        second_number = self.get_parameter_value(self.parameter_modes[1], self.idx + 2)

        if self.debug:
            print("Opcode 7:", first_number, "<", second_number, "=", int(first_number < second_number))
        self.write_value_to_address(int(first_number < second_number), self.sequence[self.idx + 3], self.parameter_modes[2])
        if self.debug: print()

        return True

    def run_opcode_8(self):
        first_number = self.get_parameter_value(self.parameter_modes[0], self.idx + 1)
        second_number = self.get_parameter_value(self.parameter_modes[1], self.idx + 2)

        if self.debug:
            print("Opcode 8:", first_number, "==", second_number, "=", int(first_number == second_number))
        self.write_value_to_address(int(first_number == second_number), self.sequence[self.idx + 3], self.parameter_modes[2])
        if self.debug: print()

        return True

    def run_opcode_9(self):
        number = self.get_parameter_value(self.parameter_modes[0], self.idx + 1)
        self.relative_base += number

        if self.debug:
            print("Opcode 9: Change relative base by", number, "to", self.relative_base)
            print()

        return True

    def run_opcode_99(self):
        self.finished = True

        if self.debug:
            print("Opcode 99: Intcode program finished")
            print()

        return True

    def process_opcode(self):
        self.opcode = self.get_opcode()
        self.parameter_modes = self.get_parameter_modes()
        # print(self.idx, self.opcode, self.sequence[self.idx:self.idx+self.opcode_length[opcode]])
        if self.debug:
            print('---', self.count, self.sequence[self.idx:self.idx + self.opcode_length[self.opcode]], '---')
        increase_idx = eval('self.run_opcode_'+str(self.opcode))()
        self.count += 1

        if increase_idx:
            self.idx += self.opcode_length[self.opcode]

    def run_intcode_program_in_command_line(self):
        while not self.finished:
            self.process_opcode()
            if self.opcode == 4:
                print("The output value is equal to", self.output[-1])
        print("Intcode program finished")

    def run_intcode_program_in_other_program(self):
        while not self.finished:
            if self.sequence[self.idx] == 3 and self.input == []:
                return False
            self.process_opcode()
        return True


if __name__ == '__main__':
    import sys
    from colorama import init
    init(autoreset=True)

    f = open(sys.argv[1], 'r')
    file_content = f.read().split(',')
    f.close()

    intcode = IntcodeProgram([int(number) for number in file_content])
    intcode.run_intcode_program_in_command_line()


