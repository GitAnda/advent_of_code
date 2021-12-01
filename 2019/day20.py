import queue


class Maze:

    def __init__(self, file_name , max_r, max_c):
        self.max_r = max_r
        self.max_c = max_c

        maze = {}
        portals = {}

        with open(file_name, 'r') as f:
            rows = [line.replace(' ', '#') + '#'*(125-len(line)) for line in f.read().split('\n')]

        for r, row in enumerate(rows):
            for c, elem in enumerate(row):

                if elem == '.' or elem == '#':
                    maze[(r, c)] = elem

                if elem.isupper():
                    if c > 0:
                        elem_left = rows[r][c-1]
                        if elem_left == '.':
                            portal_code = elem + rows[r][c+1]
                            maze[(r, c)] = portal_code
                            maze[(r, c+1)] = '#'
                            if portal_code in portals:
                                portals[portal_code].append((r, c))
                            else:
                                portals[portal_code] = [(r, c)]

                    if c < self.max_c:
                        elem_right = rows[r][c+1]
                        if elem_right == '.':
                            portal_code = rows[r][c-1] + elem
                            maze[(r, c)] = portal_code
                            maze[(r, c-1)] = '#'
                            if portal_code in portals:
                                portals[portal_code].append((r, c))
                            else:
                                portals[portal_code] = [(r, c)]

                    if r > 0:
                        elem_up = rows[r-1][c]
                        if elem_up == '.':
                            portal_code = elem + rows[r+1][c]
                            maze[(r, c)] = portal_code
                            maze[(r+1, c)] = '#'
                            if portal_code in portals:
                                portals[portal_code].append((r, c))
                            else:
                                portals[portal_code] = [(r, c)]

                    if r < self.max_r:
                        elem_down = rows[r+1][c]
                        if elem_down == '.':
                            portal_code = rows[r-1][c] + elem
                            maze[(r, c)] = portal_code
                            maze[(r-1, c)] = '#'
                            if portal_code in portals:
                                portals[portal_code].append((r, c))
                            else:
                                portals[portal_code] = [(r, c)]

        self.maze = maze
        self.portals = portals
        self.distances = {portal_code: {} for portal_code in portals}

    def print_maze(self):
        print('    ' + ''.join([str(x // 100) for x in range(self.max_c + 1)]))
        print('    ' + ''.join([str(x % 100 // 10) for x in range(self.max_c + 1)]))
        print('    ' + ''.join([str(x % 10) for x in range(self.max_c + 1)]))
        print()

        for r in range(self.max_r+1):
            if r < 10:
                line = '  ' + str(r) + ' '
            elif r < 100:
                line = ' ' + str(r) + ' '
            else:
                line = str(r) + ' '

            for c in range(self.max_c+1):
                if (r, c) in self.maze:
                    elem = self.maze[(r, c)]
                    line += elem if len(elem) == 1 else elem[0]
                else:
                    line += ' '

            print(line)

    def prune_maze(self):
        for r in range(self.max_r + 1):
            for c in range(self.max_c + 1):
                if (r, c) in self.maze and self.maze[(r, c)] == '.':
                    dead_end, _ = self.is_dead_end(r, c)
                    if dead_end:
                        self.remove_dead_end(r, c)

    def get_distances(self):
        for portal_code in self.portals:
            self.find_distances_from_portal(portal_code)

    def is_dead_end(self, r, c):
        neighbours = [self.maze[(r + 1, c)], self.maze[(r - 1, c)], self.maze[(r, c - 1)], self.maze[(r, c + 1)]]

        if neighbours.count('#') == 3:
            idx = neighbours.index('.')
            coordinates = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
            return True, coordinates[idx]

        return False, (None, None)

    def remove_dead_end(self, r, c):
        while True:
            dead_end, (new_r, new_c) = self.is_dead_end(r, c)
            if not dead_end:
                break
            self.maze[(r, c)] = '#'
            r, c = new_r, new_c

    def find_distances_from_portal(self, portal_code):
        for location in self.portals[portal_code]:
            visited_locations = set()
            q = queue.Queue()
            q.put((location, 0))
            while not q.empty():
                (r, c), d = q.get()
                neighbours = self.get_path_neighbours(r, c)
                for neighbour_location, elem in neighbours:
                    if elem.isupper():
                        if portal_code != elem:
                            self.distances[portal_code][elem] = d
                            # print('Distance between', portal_code, 'and', elem, 'is', d)
                    else:
                        if neighbour_location not in visited_locations:
                            q.put((neighbour_location, d+1))
                            # print('Add', neighbour_location, 'to queue with distance', d)
                visited_locations.add((r, c))

    def get_path_neighbours(self, r, c):
        res = []
        neighbours = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
        for (rn, cn) in neighbours:
            elem = self.maze[(rn, cn)]
            if elem == '.' or elem.isupper():
                res.append(((rn, cn), elem))
        return res

    def prune_distances(self):
        remove_distances = set()
        for portal_code in self.distances:
            if portal_code not in {'AA', 'ZZ'} and len(self.distances[portal_code]) == 2:
                # print(self.distances[portal_code])
                portal_1, portal_2 = self.distances[portal_code].keys()
                d = sum(self.distances[portal_code].values())
                remove_distances.add(portal_code)
                self.distances[portal_1][portal_2] = d
                self.distances[portal_2][portal_1] = d
                self.distances[portal_1].pop(portal_code)
                self.distances[portal_2].pop(portal_code)

        for portal_code in remove_distances:
            self.distances.pop(portal_code)

    def find_shortes_path(self):
        shortest_distances = {portal: float('inf') for portal in self.distances}

        q = queue.Queue()
        q.put((['AA'], 0))
        while not q.empty():
            path, d = q.get()

            if shortest_distances[path[-1]] < d:
                continue

            for next_portal in self.distances[path[-1]]:
                if next_portal not in path:
                    print(path, d, next_portal)
                    new_d = d + self.distances[path[-1]][next_portal]
                    if new_d < shortest_distances[next_portal]:
                        new_path = path + [next_portal]
                        q.put((new_path, new_d))
                        shortest_distances[next_portal] = new_d
                        # print('   Path', new_path, 'with distance', new_d, 'added to queue')

        return shortest_distances['ZZ']


if __name__ == '__main__':
    maze = Maze('day20.txt', 128, 124)
    # maze = Maze('day20_test.txt', 36, 34)

    maze.prune_maze()
    maze.print_maze()
    maze.get_distances()
    maze.prune_distances()
    print()
    print(maze.distances)
    print()
    # print(maze.find_shortes_path()-1)

