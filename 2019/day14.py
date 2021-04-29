def fuel_calculator(filename='day14.txt'):
    f = open(filename, 'r')
    puzzle_input = f.read().strip().split('\n')
    f.close()

    reactions = {}
    fuel_to_ore = {'ORE':[]}
    ore_to_fuel = {'FUEL':[]}
    for r in puzzle_input:
        x, y = r.split(' => ')
        yt = tuple(y.split())
        xt = [tuple(item.split()) for item in x.split(', ')]
        reactions[yt[1]] = (int(yt[0]), {c:int(n) for n,c in xt})
        fuel_to_ore[yt[1]] = [item[1] for item in xt]
        for _, chem in xt:
            ore_to_fuel[chem] = ore_to_fuel[chem] + [yt[1]] if chem in ore_to_fuel else [yt[1]]

    def ore_calculator(fuel=1):
        queue = set(fuel_to_ore['FUEL'])
        amounts = {'FUEL' : fuel}

        # i = 0
        while 'ORE' not in amounts:
            # print('ITERATION', i)
            # i += 1
            # print('Queue:', queue)
            # print('Amounts:', amounts)
            # print()
            add_queue = []
            rem_queue = []
            for chem in queue:
                dependencies = ore_to_fuel[chem]
                # print(chem, dependencies)
                # print(all([dep in amounts for dep in dependencies]))
                if all([dep in amounts for dep in dependencies]):
                    rem_queue.append(chem)
                    add_queue += fuel_to_ore[chem]

                    sum = 0
                    for dep in dependencies:
                        N, products = reactions[dep]
                        sum += products[chem] * -(-amounts[dep] // N)
                    amounts[chem] = sum
                #     print('Amount of chemical', chem, 'needed:', sum)
                # print()

            queue = queue.difference(rem_queue)
            queue = queue.union(add_queue)

        return amounts['ORE']

    ore_per_fuel = ore_calculator()

    print('---Part One---')
    print('Amount of ORE needed:', ore_per_fuel)
    print()

    print('---Part Two---')
    ore = pow(10,12)
    fuel_guess = ore // ore_per_fuel

    for _ in range(4):
        ore_guess = ore_calculator(fuel_guess)
        if ore // (ore_guess // fuel_guess) == fuel_guess:
            if ore_guess > ore:
                fuel_guess -= 1
            print('Amount of ORE needed for', fuel_guess, 'fuel:', ore_calculator(fuel_guess))
            print('Maximum amount of FUEL produced by', ore, 'ORE:', fuel_guess)
            break
        print('Amount of ORE needed for', fuel_guess, 'fuel:', ore_calculator(fuel_guess))
        fuel_guess = ore // (ore_guess // fuel_guess)



if __name__ == '__main__':
    fuel_calculator('day14.txt')