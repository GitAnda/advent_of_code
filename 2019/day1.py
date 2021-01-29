def read_input(filename):
    f = open(filename, 'r')
    file_content = f.read().split('\n')
    f.close()
    return [int(line) for line in file_content]


def get_total_fuel_for_mass(mass):
    fuel_for_mass = mass // 3 - 2
    if fuel_for_mass <= 0:
        return 0
    else:
        return fuel_for_mass + get_total_fuel_for_mass(fuel_for_mass)


def get_total_fuel_for_spacecraft(module_masses):
    return sum(map(get_total_fuel_for_mass, module_masses))


def get_fuel_for_module(module_mass):
    return module_mass // 3 - 2


def get_fuel_for_spacecraft(module_masses):
    return sum(map(get_fuel_for_module, module_masses))


def test_get_fuel_for_module():
    test_cases = {12: 2, 14: 2, 1969: 966, 100756: 50346}
    return all([get_total_fuel_for_mass(test_mass) == test_cases[test_mass] for test_mass in test_cases])


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Supply the input filename as a command line argument.")
        sys.exit()
    
    if not test_get_fuel_for_module():
        print("Check function get_fuel_for_module: something went wrong.")
        sys.exit()

    module_masses = read_input("day1.txt")
    
    print('Exercise 1.1')
    required_fuel = get_fuel_for_spacecraft(module_masses)
    print('The required fuel for the spacecraft is', required_fuel)

    print('\nExercise 1.2')
    required_fuel = get_total_fuel_for_spacecraft(module_masses)
    print('The total required fuel for the spacecraft is', required_fuel)

