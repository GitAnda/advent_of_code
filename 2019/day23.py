from Intcode import IntcodeProgram
import sys


with open("day23.txt") as f:
    initial_sequence = [int(x) for x in f.read().strip().split(',')]


class Computer:
    def __init__(self, address):
        self.intcode = IntcodeProgram(initial_sequence)
        # self.intcode.debug = True
        self.intcode.add_input(address)
        self.address = address
        self.count_empty_queue = 0
        self.idle = None

    def send(self):
        self.idle = False
        return self.intcode.get_output(size=3, extract=True)

    def receive(self, x, y):
        self.idle = False
        self.intcode.add_input((x, y))

    def run(self):
        if self.intcode.sequence[self.intcode.idx] == 3 and self.intcode.input == []:
            self.intcode.add_input(-1)
            self.count_empty_queue += 1
            self.idle = True
            # print(f'Computer {self.address} asked for input but queue is empty')
        self.intcode.process_opcode()


class ComputerNetwork:
    def __init__(self):
        self.computers = [Computer(address) for address in range(50)]
        self.nat = (None, None)
        self.send_to_computer_0 = (None, None)

    def run_all_computers_once(self):
        for computer in self.computers:
            if not computer.intcode.finished:
                computer.run()

                while len(computer.intcode.output) > 2:
                    to_address, x, y = computer.send()
                    if to_address == 255:
                        # print(f'Sending to NAT packet {(x, y)}')
                        self.nat = (x, y)
                    else:
                        # print(f'Sending to computer {to_address} packet {(x, y)}')
                        to_computer = self.computers[to_address]
                        to_computer.receive(x, y)

    def all_computers_idle(self):

        return all([computer.idle and computer.count_empty_queue > 1 for computer in self.computers])

    def run(self):
        count = 0
        while True:
            # print('---', count, '---')
            self.run_all_computers_once()

            if self.all_computers_idle():
                print(f'All computers idle: sending to computer 0 packet {self.nat}')
                if self.send_to_computer_0[1] == self.nat[1]:
                    return
                self.send_to_computer_0 = self.nat
                self.computers[0].intcode.add_input(self.nat)
                self.computers[0].idle = False

            # if self.nat[1]:
            #     return
            # count += 1


if __name__ == '__main__':
    network = ComputerNetwork()
    network.run()














