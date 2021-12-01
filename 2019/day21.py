from Intcode import IntcodeProgram

with open("day21.txt") as f:
    sequence = [int(x) for x in f.read().strip().split(',')]


def part_1():
    print('Part 1:')

    with open("day21_input_part1.txt") as f:
        program = [ord(x) for x in f.read()]

    robot = IntcodeProgram(sequence)
    robot.add_input(program)
    robot.run_intcode_program_in_other_program()
    print(''.join([chr(x) if x < 256 else str(x) for x in robot.output]))


def part_2():
    print('Part 2:')

    with open("day21_input_part2.txt") as f:
        program = [ord(x) for x in f.read()]

    robot = IntcodeProgram(sequence)
    robot.add_input(program)
    robot.run_intcode_program_in_other_program()
    print(''.join([chr(x) if x < 256 else str(x) for x in robot.output]))


if __name__ == '__main__':
    part_1()
    part_2()














