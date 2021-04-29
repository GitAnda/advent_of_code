class SimpleGame:
    tile_dict = {0: ' ', 1: '*', 2: '#', 3: '=', 4: 'o'}

    def __init__(self, sequence):
        from Intcode import IntcodeProgram
        self.intcode = IntcodeProgram(sequence)
        self.screen = []

    def count_blocks(self):
        count = 0
        for row in self.screen:
            count += row.count('#')

        return count

    def draw_screen(self):
        self.screen = [['.' for _ in range(max([x for i,x in enumerate(self.intcode.output) if i%3 == 0])+1)] for _ in range(max([x for i,x in enumerate(self.intcode.output) if i%3 == 1])+1)]
        score = 0
        for i in range(0,len(self.intcode.output),3):
            tile_id = self.intcode.output[i+2]
            # tile_dict = {0: ' ', 1: '*', 2: '#', 3: '-', 4: 'o'}
            if self.intcode.output[i] == -1:
                score = tile_id
            else:
                self.screen[self.intcode.output[i+1]][self.intcode.output[i]] = self.tile_dict[tile_id]

        count = self.count_blocks()
        print('Blocks left: ', count, '   Score: ', score)
        for row in self.screen:
            print(''.join(row))

        return count

    def play_game(self):
        import msvcrt

        number_of_blocks = self.draw_screen()
        while number_of_blocks > 0 and self.intcode.finished is False:
            user_input = msvcrt.getch().decode("utf-8")
            if user_input == 'a':
                self.intcode.add_input(-1)
            elif user_input == 'd':
                self.intcode.add_input(1)
            else:
                self.intcode.add_input(0)
            self.intcode.run_intcode_program_in_other_program()
            number_of_blocks = self.draw_screen()


if __name__ == '__main__':

    f = open('day13.txt', 'r')
    initial_sequence = [int(x) for x in f.read().strip().split(',')]
    f.close()

    game = SimpleGame(initial_sequence)
    game.intcode.sequence[0] = 2
    game.intcode.run_intcode_program_in_other_program()
    game.play_game()