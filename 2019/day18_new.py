class Node:
    def __init__(self, path, distance, maze):
        self.path = path
        self.distance = distance
        self.maze_state = maze

class Tree:
    def __init__(self, initial_maze):
        self.queue = []
        self.initial_maze = initial_maze
        self.keys_and_doors = {item: location for location, item in self.initial_maze.items() if item != '.'}
        self.distance_matrix = self.make_matrix()

    def make_matrix(self):
        matrix = {}
        matrix.update(self.distances_to('@', self.initial_maze))
        for char in self.keys_and_doors:
            if char.islower():
                matrix.update(self.distances_to(char, self.initial_maze))

        return matrix

    def distances_to(self, key, maze):
        distance_matrix = {}
        distances = [(self.keys_and_doors[key], 0, set())]

        visited_locations = set()
        while distances:
            new_distances = []
            for i, item in enumerate(distances):
                coordinate, distance, doors = item
                visited_locations.add(coordinate)

                new_locations = self.expand_location(coordinate)
                new_locations = new_locations.difference(visited_locations)
                for new_location in new_locations:
                    char = maze[new_location]
                    if char == '.':
                        new_distances.append((new_location, distance+1, doors))
                    elif char.isupper():
                        new_doors = doors.copy()
                        new_doors.add(char.lower())
                        new_distances.append((new_location, distance + 1, new_doors))
                    elif char.islower():
                        distance_matrix[(key, char)] = (distance + 1, doors)

            distances = new_distances

        return distance_matrix

    def expand_location(self, coordinate):
        x, y = coordinate
        adjacent = set()
        if (x + 1, y) in self.initial_maze.keys():
            adjacent.add((x + 1, y))
        if (x - 1, y) in self.initial_maze.keys():
            adjacent.add((x - 1, y))
        if (x, y + 1) in self.initial_maze.keys():
            adjacent.add((x, y + 1))
        if (x, y - 1) in self.initial_maze.keys():
            adjacent.add((x, y - 1))
        return adjacent

    def expand_node(self, node):
        distances = self.distances_to(node.path[-1], node.maze_state)
        # keys = set(node.path)
        # for key_from, key_to in self.distance_matrix:
        #     if key_from in keys:
        #

        for key_from, key_to in distances:

            dist, doors = distances[(key_from, key_to)]
            if doors.issubset(set(node.path)):
                new_path = node.path + (key_to,)
                new_distance = node.distance + dist
                new_maze = node.maze_state.copy()
                new_maze[self.keys_and_doors[key_from]] = '.'
                new_node = Node(new_path, new_distance, new_maze)
                self.add_node_to_queue(new_node)

    def add_node_to_queue(self, node):
        self.queue.append(node)

    def get_node_from_queue(self):
        node = self.queue[-1]
        self.queue.pop(-1)
        return node

    def find_shortest_distance(self):
        logbook = {}

        def keys_in_logbook(keys):
            for path in logbook.keys():
                if set(keys).issubset(set(path)):
                    return True, path
            return False, tuple()

        initial_node = Node(('@',), 0, self.initial_maze)
        self.add_node_to_queue(initial_node)

        count = 0
        while self.queue:
            node = self.get_node_from_queue()
            # print('Node:', node.path, node.distance)
            in_logbook, logbook_key = keys_in_logbook(node.path)

            if in_logbook:
                path, dist = logbook[logbook_key]
                if node.distance < dist:
                    logbook[logbook_key] = (node.path, node.distance)
            else:
                logbook[node.path] = (node.path, node.distance)

            self.expand_node(node)
            count += 1
            if count % 100 == 0:
                print(count, len(self.queue), end='\r')
                break

        all_keys = tuple([char for char in self.keys_and_doors if char.islower()])
        in_logbook, logbook_key = keys_in_logbook(all_keys)
        if in_logbook:
            path, dist = logbook[logbook_key]
            print('Shortest distance is', dist, 'via path', path)
        else:
            print('Solution not found.')
            for path, distance in logbook.values():
                print(path, ':', distance)


if __name__ == '__main__':
    from day18_prune import *
    import cProfile

    maze = get_pruned_maze()
    for coordinate in ((39,40), (41,40), (40,39), (40,41)):
        maze[coordinate] = '.'

    print_map(maze)
    tree = Tree(maze)
    print(tree.distance_matrix)
    # tree.find_shortest_distance()
    # cProfile.run("tree.find_shortest_distance()")






