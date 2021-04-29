class Moon:

    def __init__(self, initial_location):
        self.location = initial_location
        self.velocity = [0, 0, 0]

    def __repr__(self):
        return 'Moon(loc=' + str(self.location) + ', vel=' + str(self.velocity) + ')'

    def state_of_the_moon(self, axis):
        string = ''
        string += ':' + str(self.location[axis])
        string += ':' + str(self.velocity[axis])

        return string


class MotionSimulator:

    def __init__(self, initial_moons):
        self.moons = initial_moons
        self.previous_states = set()

    def apply_gravity(self, x):
        for i in range(len(self.moons)):
            for j in range(i):
                if self.moons[i].location[x] < self.moons[j].location[x]:
                    self.moons[i].velocity[x] += 1
                    self.moons[j].velocity[x] -= 1
                elif self.moons[i].location[x] > self.moons[j].location[x]:
                    self.moons[i].velocity[x] -= 1
                    self.moons[j].velocity[x] += 1

    def apply_velocity(self, x):
        for moon in self.moons:
            moon.location[x] += moon.velocity[x]

    def find_total_energy(self):
        total_energy = 0
        for moon in self.moons:
            potential_energy = abs(moon.location[0]) + abs(moon.location[1]) + abs(moon.location[2])
            kinetic_energy = abs(moon.velocity[0]) + abs(moon.velocity[1]) + abs(moon.velocity[2])
            total_energy += potential_energy * kinetic_energy

        return total_energy

    def apply_time_steps(self, number, axis):
        for i in range(number):
            self.apply_gravity(axis)
            self.apply_velocity(axis)
            # print('Iteration', i, end='r')

    def find_previous_state(self):
        periods = []
        for x in range(3):
            i = 0
            self.previous_states = set()
            print('Axis', x)
            print(self.state_of_the_universe(x))
            while True:
                self.previous_states.add(self.state_of_the_universe(x))
                if i == 0:
                    print(self.state_of_the_universe(x))
                self.apply_time_steps(1, x)
                # print('Iteration', i, end='\r')
                i += 1

                if self.state_of_the_universe(x) in self.previous_states:
                    break

            periods.append(i)
            print('Iteration', i)
        return periods

    def find_repeating_period(self):
        periods = self.find_previous_state()
        max_period = max(periods)
        periods.remove(max_period)

        i = 1
        while (max_period*i) % periods[0] != 0 or (max_period*i) % periods[1] != 0:
            i += 1

        print(max_period*i)

    def state_of_the_universe(self, axis):
        string = ''
        for moon in self.moons:
            string += moon.state_of_the_moon(axis)

        return string


if __name__ == '__main__':
    import sys

    f = open(sys.argv[1])
    file_content = f.read().strip().split('\n')
    f.close()

    moons = []
    for line in file_content:
        location = [int(x) for x in line.replace('<','').replace('>','').replace('x=','').replace('y=','').replace('z=','').strip().split(',')]
        moons.append(Moon(location))

    moons_of_jupiter = MotionSimulator(moons)
    # moons_of_jupiter.apply_time_steps(1000, 0)
    # moons_of_jupiter.apply_time_steps(1000, 1)
    # moons_of_jupiter.apply_time_steps(1000, 2)
    # print(moons_of_jupiter.find_total_energy())

    # print(moons_of_jupiter.previous_states)

    moons_of_jupiter.find_repeating_period()



