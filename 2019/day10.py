class AsteroidMap:

    def __init__(self, filename):
        f = open(filename, 'r')
        file_content = f.read().strip().split('\n')
        f.close()

        self.asteroid_map = [[x for x in line] for line in file_content]
        self.locations_asteroids = self.find_locations_asteroids()
        self.distance_matrix = self.get_distance_matrix()

    def __str__(self):
        for row in self.asteroid_map:
            print(''.join(row))

    def find_locations_asteroids(self):
        locations = []
        n = 0
        for i in range(len(self.asteroid_map)):
            for j in range(len(self.asteroid_map[0])):
                if self.asteroid_map[i][j] == '#':
                    locations.append((n, i, j))
                    n += 1

        return locations

    def get_distance_matrix(self):
        distance_matrix = [[0 for _ in self.locations_asteroids] for _ in self.locations_asteroids]
        for a, asteroid_a in enumerate(self.locations_asteroids):
            for b, asteroid_b in enumerate(self.locations_asteroids):
                dx = asteroid_b[1] - asteroid_a[1]
                dy = asteroid_b[2] - asteroid_a[2]
                distance_matrix[asteroid_a[0]][asteroid_b[0]] = (dx, dy)

        return distance_matrix

    def find_number_of_asteroids_in_sight(self, asteroid_id):
        from math import gcd, asin
        distances_relative_to_asteroid = self.distance_matrix[asteroid_id][:asteroid_id] + self.distance_matrix[asteroid_id][asteroid_id+1:]
        normalised_distances = [(x / gcd(x, y), y / gcd(x, y)) for x, y in distances_relative_to_asteroid]

        return len(set(normalised_distances))

    def find_200th_astroid(self):
        from math import atan2, pi
        asteroid, number_of_visible_asteroids = self.find_best_asteroid_for_station()
        asteroid_id = asteroid[0]
        distances_relative_to_asteroid = self.distance_matrix[asteroid_id][:asteroid_id] + self.distance_matrix[asteroid_id][asteroid_id+1:]

        distances_with_angle = sorted([(-atan2(x, y)+pi, y, x) for y, x in distances_relative_to_asteroid])
        # print(distances_with_angle)

        print(len(set([(-atan2(x, y)+pi) for y, x in distances_relative_to_asteroid])))
        # for x in normalised_distances:
        #     print(x)
        #
        # return len(set(normalised_distances))

    def find_best_asteroid_for_station(self):
        max_asteroids_in_sight = 0
        for asteroid in self.locations_asteroids:
            if self.find_number_of_asteroids_in_sight(asteroid[0]) > max_asteroids_in_sight:
                max_asteroids_in_sight = self.find_number_of_asteroids_in_sight(asteroid[0])
                best_asteroid = asteroid

        return best_asteroid, max_asteroids_in_sight

    def print_best_asteroid(self):
        from termcolor import colored
        from colorama import init
        init(autoreset=True)

        best_asteroid, max_asteroids_in_sight = self.find_best_asteroid_for_station()
        print(colored(best_asteroid, 'red'))

        count = 0
        for i in range(len(self.asteroid_map)):
            for j in range(len(self.asteroid_map[0])):
                if self.asteroid_map[i][j] == '#':
                    print(colored(self.asteroid_map[i][j], 'red'), end='') if count == best_asteroid[0] else print(self.asteroid_map[i][j], end='')
                    count += 1
                else:
                    print(self.asteroid_map[i][j], end='')
            print('\n', end='')


if __name__ == '__main__':
    import sys

    map_asteroids = AsteroidMap(sys.argv[1])
    map_asteroids.print_best_asteroid()
    map_asteroids.find_200th_astroid()



