class MapTree:

    def __init__(self, maze, initial_location):
        self.nodes = set()
        self.initial_coordinate = initial_location
        self.map = maze
        self.undiscovered = set(maze.keys())
        self.undiscovered.remove(initial_location)
        self.expand_node(MapNode(self.initial_coordinate))

    def expand_node(self, node):
        next_coordinate = set()
        next_coordinate.add(node.begin)
        valuable = False
        while len(next_coordinate) == 1 and not valuable:
            next_coordinate = next_coordinate.pop()
            node.add_coordinate(next_coordinate)

            if self.map[next_coordinate] != '.':
                node.add_valuable(self.map[next_coordinate])
                valuable = True

            next_coordinate = self.get_adjacent_coordinate(next_coordinate)

        node.set_length()

        downstream_valuables = set()
        if len(next_coordinate) >= 1:
            for coordinate in next_coordinate:
                child = MapNode(coordinate)
                child.parent = node
                downstream_valuables = downstream_valuables.union(self.expand_node(child))

        node.downstream = downstream_valuables

        self.nodes.add(node)

        if node.valuable:
            downstream_valuables.add(node.valuable)

        return downstream_valuables

    def get_adjacent_coordinate(self, coordinate):
        x, y = coordinate
        adjacent = set()
        if (x + 1, y) in self.undiscovered:
            adjacent.add((x + 1, y))
            self.undiscovered.remove((x + 1, y))
        if (x - 1, y) in self.undiscovered:
            adjacent.add((x - 1, y))
            self.undiscovered.remove((x - 1, y))
        if (x, y + 1) in self.undiscovered:
            adjacent.add((x, y + 1))
            self.undiscovered.remove((x, y + 1))
        if (x, y - 1) in self.undiscovered:
            adjacent.add((x, y - 1))
            self.undiscovered.remove((x, y - 1))
        return adjacent

    def prune(self):
        for node in self.nodes:
            if not node.downstream or all([char.isupper() for char in node.downstream]):
                for coordinate in node.coordinates:
                    self.map.pop(coordinate)

        self.nodes = set()
        self.undiscovered = set(self.map.keys())
        self.undiscovered.remove(self.initial_coordinate)
        self.expand_node(MapNode(self.initial_coordinate))

        # for i, node in enumerate(self.nodes):
        #     print()
        #     print(node.length, node.valuable)
        #     print('Downstream:', node.downstream)


def get_pruned_maze():
    maze = {}

    with open('day18.txt', 'r') as f:
        rows = [line for line in f.read().strip().split('\n')]
        for r, row in enumerate(rows):
            for c, elem in enumerate(row):
                if elem != '#':
                    maze[(r, c)] = elem
                if elem == '@':
                    initial_location = (r, c)

    r, c = initial_location

    maze_tree = MapTree(maze, initial_location)
    maze_tree.prune()
    return maze_tree.map


def print_map(maze):
    r_min, c_min, r_max, c_max = float('inf'), float('inf'), 0, 0
    for x, y in maze.keys():
        if x < r_min: r_min = x
        if x > r_max: r_max = x
        if y < c_min: c_min = y
        if y > c_max: c_max = y

    for x in range(r_max-r_min+1):
        row = []
        for y in range(c_max-c_min+1):
            if (x + r_min, y + c_min) in maze.keys():
                row.append(maze[(x + r_min, y + c_min)])
            else:
                row.append(' ')
        print(' '.join(row))


class MapNode:
    def __init__(self, initial_coordinate):
        self.begin = initial_coordinate
        self.valuable = None
        self.coordinates = set()
        self.parent = None
        self.length = None
        self.downstream = set()

    def add_coordinate(self, coordinate):
        self.coordinates.add(coordinate)

    def add_valuable(self, valuable):
        self.valuable = valuable

    def set_length(self):
        self.length = len(self.coordinates)


if __name__ == '__main__':
    print_map(get_pruned_maze())

