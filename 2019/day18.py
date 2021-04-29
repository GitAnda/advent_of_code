import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 102, 204)
YELLOW = (0, 102, 204)
GREY = (127, 127, 127)
LIGHTGREY = (80, 80, 80)

class Maze:
    moves = {'NORTH': 1, 'SOUTH': 2, 'WEST': 3, 'EAST': 4}
    print_status = {'#': 'WALL', 1: 'MOVE', 2: 'GOAL', 3: 'START'}
    direction = ['NORTH', 'WEST', 'SOUTH', 'EAST']

    def __init__(self, maze, initial_location):
        self.screen_size = (810, 810)
        self.block_size = 10
        # self.offset = [(x // 20) * 10 for x in self.screen_size]
        self.offset = (0, 0)

        self.loc = initial_location
        self.map = maze
        self.idx = 0

        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.draw_initial_screen()
        pygame.display.set_caption("My First Game")
        self.clock = pygame.time.Clock()
        self.carry_on = True
        self.algorithm = False

        self.move = None
        self.status = None

    def run_game(self):

        while self.carry_on:
            if self.algorithm:
                self.keep_right()
            else:
                self.capture_events()

            if self.move:
                self.update_screen()

                if self.status:
                    self.loc = self.new_location()
                    self.idx = (self.idx - 1) % 4
                else:
                    self.idx = (self.idx + 1) % 4

            pygame.display.flip()

            self.clock.tick(60)
            self.move, self.status = None, None

        pygame.quit()

    def keep_right(self):
        self.move = self.direction[self.idx]

        if self.new_location() == (0, 0) and self.idx == 0:
            self.algorithm = False

    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.carry_on = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.move = 'SOUTH'
                if event.key == pygame.K_UP:
                    self.move = 'NORTH'
                if event.key == pygame.K_LEFT:
                    self.move = 'WEST'
                if event.key == pygame.K_RIGHT:
                    self.move = 'EAST'

    def draw_initial_screen(self):
        self.screen.fill(GREY)

        x, y = self.screen_size
        for i in range(1, x//self.block_size):
            pygame.draw.line(self.screen, LIGHTGREY, [i*self.block_size, 0], [i*self.block_size, y], 1)
        for i in range(1, y//self.block_size):
            pygame.draw.line(self.screen, LIGHTGREY, [0, i*self.block_size], [x, i*self.block_size], 1)

        for location, tile in self.map.items():
            x, y = [l+o for l, o in zip(location, self.offset)]
            self.draw_tile(x*self.block_size, y*self.block_size, tile)

        b = self.block_size
        xs, ys = [l + o for l, o in zip(self.loc, self.offset)]
        pygame.draw.rect(self.screen, YELLOW, [xs + 3, ys + 3, b - 5, b - 5])

    def draw_tile(self, x, y, tile_type):
        b = self.block_size
        if tile_type == '@':
            pygame.draw.rect(self.screen, YELLOW, [x, y, b + 1, b + 1], 1)
            pygame.draw.rect(self.screen, WHITE, [x + 1, y + 1, b - 1, b - 1])
        elif tile_type.islower():
            pygame.draw.rect(self.screen, WHITE, [x + 1, y + 1, b - 1, b - 1])
            pygame.draw.rect(self.screen, GREEN, [x + 3, y + 3, b - 5, b - 5])
        elif tile_type.isupper():
            pygame.draw.rect(self.screen, GREEN, [x + 1, y + 1, b - 1, b - 1])
        elif tile_type == '.':
            pygame.draw.rect(self.screen, WHITE, [x + 1, y + 1, b - 1, b - 1])
        elif tile_type == '#':
            pygame.draw.rect(self.screen, BLACK, [x + 1, y + 1, b - 1, b - 1])

    def new_location(self):
        if self.move == 'NORTH':
            return self.loc[0], self.loc[1] - self.block_size
        elif self.move == 'SOUTH':
            return self.loc[0], self.loc[1] + self.block_size
        elif self.move == 'WEST':
            return self.loc[0] - self.block_size, self.loc[1]
        elif self.move == 'EAST':
            return self.loc[0] + self.block_size, self.loc[1]
        return self.loc

    def update_screen(self):
        new_x, new_y = [l+o for l, o in zip(self.new_location(), self.offset)]
        b = self.block_size

        self.draw_tile(new_x, new_y, self.status)

        if self.status:
            x, y = [l+o for l, o in zip(self.loc, self.offset)]
            self.draw_tile(x, y, self.map[self.loc])
            pygame.draw.rect(self.screen, YELLOW, [new_x + 3, new_y + 3, b - 5, b - 5])


if __name__ == '__main__':
    maze = {}

    with open('day18.txt', 'r') as f:
        rows = [line for line in f.read().strip().split('\n')]
        for c, row in enumerate(rows):
            print_row = row.replace('#', ' ')
            # print(' '.join([char for char in print_row]))
            for r, elem in enumerate(row):
                maze[(r, c)] = elem
                if elem == '@':
                    initial_location = (r, c)

    # print(initial_location)
    game = Maze(maze, initial_location)
    game.run_game()

