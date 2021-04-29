from Intcode import IntcodeProgram


def get_map(sequence):

    intcode = IntcodeProgram(sequence)
    intcode.run_intcode_program_in_other_program()

    for i, x in enumerate(intcode.output):
        if x == 10:
            w = i+1
            break
    h = len(intcode.output) // w
    print(h,w)

    character_output = [chr(x) for x in intcode.output]
    feed = [character_output[i*w:w*(i+1)-1] for i in range(h)]
    w -= 1

    alignment = 0
    for x in range(1, w-1):
        for y in range(1, h-1):
            if feed[y][x] == '#' and feed[y+1][x] == '#' and feed[y-1][x] == '#' and feed[y][x+1] == '#' and feed[y][x-1] == '#':
                alignment += x*y
                feed[y][x] = 'O'

    print_map(feed)
    print('Part 1:', alignment, '\n')


def print_map(feed):
    for m in feed:
        print(' '.join(m))


if __name__ == '__main__':
    with open("day17.txt") as f:
        sequence = [int(x) for x in f.read().strip().split(',')]

    get_map(sequence)

    sequence[0] = 2
    robot = IntcodeProgram(sequence)

    routine = [ord(char) for char in 'A,B,B,A,C,A,C,A,C,B\n']
    A = [ord(char) for char in 'L,6,R,12,R,8\n']
    B = [ord(char) for char in 'R,8,R,12,L,12\n']
    C = [ord(char) for char in 'R,12,L,12,L,4,L,4\n']
    video = [ord(char) for char in 'n\n']

    robot.add_input(routine + A + B + C + video)
    robot.run_intcode_program_in_other_program()

    print(robot.output)








