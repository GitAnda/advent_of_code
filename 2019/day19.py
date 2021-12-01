from Intcode import IntcodeProgram

with open("day19.txt") as f:
    sequence = [int(x) for x in f.read().strip().split(',')]


def part_1():
    count = 0
    print(' '.join(['  '] + [str(x//10) for x in range(50)]))
    print(' '.join(['  '] + [str(x%10) for x in range(50)]))
    for y in range(50):
        if y < 10:
            row = [' '+str(y)]
        else:
            row = [str(y)]

        for x in range(50):
            if is_beam(x, y):
                row.append('#')
                count += 1
            else:
                row.append('.')
        print(' '.join(row))

    print('Part 1:')
    print(count)


def part_2(N = 100):
    x, y = 5, 4
    while True:
        print(x, y, end='\r')
        if is_beam(x+1, y+1):
            x += 1
            y += 1
        elif is_beam(x+1, y):
            x += 1
        else:
            print('New beam not found at expected location')
            break

        if is_beam(x + N-1, y - (N-1)):
            print('Part 2:')
            print(x, y-(N-1), x*10000+y-(N-1))
            break


def is_beam(x, y):
    robot = IntcodeProgram(sequence)
    robot.add_input([x, y])
    robot.run_intcode_program_in_other_program()
    if robot.output[-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    part_1()
    part_2()














