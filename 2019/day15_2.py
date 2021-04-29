def main():
    filename = 'day15_map.txt'

    f = open(filename, 'r')

    locations = set()
    for x in f.read().strip()[2:-1].split(', ('):
        key, value = x.split('): ')
        x, y = [int(k) for k in key.split(', ')]
        value = int(value)
        if value == 1 or value == 2:
            locations.add((x//10, y//10))

        if value == 2:
            frontier = {(x//10, y//10)}

    f.close()

    count = 0
    oxygen = set()
    while locations:
        # print('---- Time', count,'----')
        # print('Frontier:', frontier)
        oxygen = oxygen.union(frontier)

        frontier_add = set()
        for x, y in frontier:
            neighbors = locations.intersection({(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)})
            # print('Neighbors of', str((x,y)), 'are', neighbors)
            frontier_add = frontier_add.union(neighbors)
        # print('Locations with oxygen:', frontier_add)
        frontier = frontier_add
        locations = locations.difference(frontier_add)
        count += 1

    print('Minutes until fully oxynated:', count)




if __name__ == '__main__':
    main()