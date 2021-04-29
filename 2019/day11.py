class Robot:

    def __init__(self):
        self.surface = [['.' for _ in range(5)] for _ in range(5)]
        self.surface[2][2] = '#'
        self.footprint = [['.' for _ in range(5)] for _ in range(5)]
        self.robot_location = [2, 2]
        self.robot_direction = [-1, 0]

    def extend_surface(self, direction):
        if direction == [-1, 0]:
            self.surface.insert(0, ['.' for _ in self.surface[0]])
        elif direction == [1, 0]:
            self.surface.append(['.' for _ in self.surface[0]])
        elif direction == [0, -1]:
            for i in range(len(self.surface)):
                self.surface[i].insert(0, '.')
        elif direction == [0, 1]:
            for i in range(len(self.surface)):
                self.surface[i].append('.')

    def extend_footprint(self, direction):
        if direction == [-1, 0]:
            self.footprint.insert(0, ['.' for _ in self.footprint[0]])
        elif direction == [1, 0]:
            self.footprint.append(['.' for _ in self.footprint[0]])
        elif direction == [0, -1]:
            for i in range(len(self.footprint)):
                self.footprint[i].insert(0, '.')
        elif direction == [0, 1]:
            for i in range(len(self.footprint)):
                self.footprint[i].append('.')

    def paint_surface(self, intcode):
        count = 0
        while True:
            count += 1
            print()
            print(count, '         Robot location is', self.robot_location, 'with direction', self.robot_direction)
            if self.surface[self.robot_location[0]][self.robot_location[1]] == '.':
                intcode.add_input(0)
            elif self.surface[self.robot_location[0]][self.robot_location[1]] == '#':
                intcode.add_input(1)

            finished = intcode.run_intcode_program_in_other_program()

            self.surface[self.robot_location[0]][self.robot_location[1]] = '.' if intcode.output[1] == 0 else '#'
            self.footprint[self.robot_location[0]][self.robot_location[1]] = '#'
            # self.print_surface()

            if finished:
                self.print_surface()
                # self.print_footprint()
                break

            matrix = [[0, -1], [1, 0]] if intcode.output[0] == 0 else [[0, 1], [-1, 0]]
            self.robot_direction = [matrix[0][0]*self.robot_direction[0] + matrix[0][1]*self.robot_direction[1], matrix[1][0]*self.robot_direction[0] + matrix[1][1]*self.robot_direction[1]]

            self.robot_location[0] += self.robot_direction[0]
            self.robot_location[1] += self.robot_direction[1]
            if self.robot_location[0] >= len(self.surface) or self.robot_location[1] >= len(self.surface[0]):
                self.extend_surface(self.robot_direction)
                self.extend_footprint(self.robot_direction)
            if self.robot_location[0] < 0 or self.robot_location[1] < 0:
                self.extend_surface(self.robot_direction)
                self.extend_footprint(self.robot_direction)
                self.robot_location = [max(0, self.robot_location[0]), max(0, self.robot_location[1])]

    def print_surface(self):
        for row in self.surface:
            print(''.join(row))

    def print_footprint(self):
        n = 0
        for row in self.footprint:
            print(''.join(row))
            n += ''.join(row).count('#')
        print(n)



if __name__ == '__main__':
    from Intcode import IntcodeProgram
    import sys

    f = open(sys.argv[1])
    sequence = [int(x) for x in f.read().strip().split(',')]
    f.close()

    intcode = IntcodeProgram(sequence)
    # intcode.debug = True
    robot = Robot()
    robot.paint_surface(intcode)


