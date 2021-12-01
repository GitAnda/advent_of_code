from Intcode import IntcodeProgram
import re
import copy
import queue


with open("day25.txt") as f:
    initial_sequence = [int(x) for x in f.read().strip().split(',')]


class Droid:
    def __init__(self):
        self.intcode = IntcodeProgram(initial_sequence)
        self.location = None

    def run_in_command_line(self):
        while not self.intcode.finished:
            self.intcode.run_intcode_program_in_other_program()
            ascii_output = self.intcode.get_output(extract=True)
            string_output = ''.join([chr(x) for x in ascii_output])
            print(string_output)

            string_input = input("")
            ascii_input = [ord(x) for x in string_input] + [ord('\n')]
            self.intcode.add_input(ascii_input)


class Solver:
    moves = ('south', 'east', 'north', 'west')

    def __init__(self):
        self.forbidden_items = ["molten lava", "giant electromagnet", "escape pod", "infinite loop"]
        self.locations = {}
        self.queue = queue.Queue()

        self.intcode = IntcodeProgram(initial_sequence)
        self.intcode.run_intcode_program_in_other_program()
        ascii_output = self.intcode.get_output(extract=True)
        string_output = ''.join([chr(x) for x in ascii_output])
        string_output, location, directions, items = self.read_output(string_output)

        for direction in directions:
            pass

    def solve(self):
        pass

    def process(self, node):
        string_input = input("")
        ascii_input = [ord(x) for x in string_input] + [ord('\n')]
        self.intcode.add_input(ascii_input)
        self.intcode.run_intcode_program_in_other_program()
        ascii_output = self.intcode.get_output(extract=True)
        string_output = ''.join([chr(x) for x in ascii_output])

    @staticmethod
    def read_output(string_output):
        re_location = "== [a-zA-Z ]+ =="
        re_directions = "Doors here lead:\n[\w\s-]*\n\n"
        re_items = "Items here:\n[\w\s-]*\n\n"

        try:
            location = re.search(re_location, string_output).group()[3:-3]
        except AttributeError:
            location = None

        try:
            directions = re.search(re_directions, string_output).group()
            directions = directions.strip().split('\n- ')[1:]
        except AttributeError:
            directions = []

        try:
            items = re.search(re_items, string_output).group()
            items = items.strip().split('\n- ')[1:]
        except AttributeError:
            items = []

        return location, directions, items


if __name__ == '__main__':

    droid = Droid()
    droid.run_in_command_line()

    # solved it by hand
    # pick up sand, space law space brochure, wreath and fixed point and enter the cockpit














