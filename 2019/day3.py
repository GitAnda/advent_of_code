def load_wires(filename):
    f = open(filename, 'r')
    wire_a = f.readline().split(',')
    wire_b = f.readline().split(',')
    f.close()

    return wire_a, wire_b


def wire_segments_cross_at(segment_a, segment_b):
    [pos_a1, pos_a2] = segment_a
    [pos_b1, pos_b2] = segment_b

    if pos_a1[0] == pos_a2[0] and pos_b1[0] == pos_b2[0]:
        return False, [0, 0]
    if pos_a1[1] == pos_a2[1] and pos_b1[1] == pos_b2[1]:
        return False, [0, 0]

    const_a = pos_a1[0] if pos_a1[0] == pos_a2[0] else pos_a1[1]
    const_b = pos_b1[0] if pos_b1[0] == pos_b2[0] else pos_b1[1]
    interval_a = [pos_a1[1], pos_a2[1]] if pos_a1[0] == pos_a2[0] else [pos_a1[0], pos_a2[0]]
    interval_b = [pos_b1[1], pos_b2[1]] if pos_b1[0] == pos_b2[0] else [pos_b1[0], pos_b2[0]]
    interval_a.sort()
    interval_b.sort()

    if interval_a[0] < const_b < interval_a[1] and interval_b[0] < const_a < interval_b[1]:
        if pos_a1[0] == pos_a2[0]:
            return True, [const_a, const_b]
        else:
            return True, [const_b, const_a]

    return False, [0, 0]


def translate_wire_code_to_locations(wire_code):
    x = 0
    y = 0
    
    corner_positions = [[x, y]]
    for corner in wire_code:
        if corner[0] == "U":
            y = y + int(corner[1:])
        if corner[0] == "D":
            y = y - int(corner[1:])
        if corner[0] == "R":
            x = x + int(corner[1:])
        if corner[0] == "L":
            x = x - int(corner[1:])

        corner_positions += [[x, y]]
    
    return corner_positions


def distance_between_points(point, other_point):
    return abs(point[0] - other_point[0]) + abs(point[1] - other_point[1])


def find_distance_to_closest_crossed_wire(wire_a, wire_b):
    wire_a_corners = translate_wire_code_to_locations(wire_a)
    wire_b_corners = translate_wire_code_to_locations(wire_b)

    pos_closest_cross = [float("inf"), float("inf")]

    for i in range(len(wire_a_corners)-1):
        for j in range(len(wire_b_corners)-1):
            segments_cross, pos_cross = wire_segments_cross_at([wire_a_corners[i], wire_a_corners[i+1]], [wire_b_corners[j], wire_b_corners[j+1]])
            if segments_cross and distance_between_points(pos_cross, [0, 0]) < distance_between_points(pos_closest_cross, [0, 0]):
                pos_closest_cross = pos_cross
    
    return distance_between_points(pos_closest_cross, [0, 0])


def find_distance_to_first_crossed_wire(wire_a, wire_b):
    wire_a_corners = translate_wire_code_to_locations(wire_a)
    wire_b_corners = translate_wire_code_to_locations(wire_b)

    import matplotlib.pyplot as plt
    plt.plot([x[0] for x in wire_a_corners], [x[1] for x in wire_a_corners])
    plt.plot([x[0] for x in wire_b_corners], [x[1] for x in wire_b_corners])

    shortest_distance = float("inf")

    length_a = 0
    for i in range(len(wire_a_corners) - 1):
        length_b = 0
        for j in range(len(wire_b_corners) - 1):
            segments_cross, pos_cross = wire_segments_cross_at([wire_a_corners[i], wire_a_corners[i + 1]],
                                                               [wire_b_corners[j], wire_b_corners[j + 1]])
            if segments_cross:
                cross_distance = length_a + length_b + distance_between_points(pos_cross, wire_a_corners[i]) + \
                                 distance_between_points(pos_cross, wire_b_corners[j])

                plt.plot(pos_cross[0], pos_cross[1], 'ro')

                shortest_distance = min(shortest_distance, cross_distance)

            length_b += distance_between_points(wire_b_corners[j], wire_b_corners[j + 1])

        length_a += distance_between_points(wire_a_corners[i], wire_a_corners[i + 1])

    plt.show()
    return shortest_distance


if __name__ == '__main__':
    import sys

    wire_1, wire_2 = load_wires(sys.argv[1])
    
    print('Exercise 3.1')
    distance_closest_cross = find_distance_to_closest_crossed_wire(wire_1, wire_2)
    print('The closest crossed wire is', distance_closest_cross, 'away from the central port')

    print('\nExercise 3.2')
    distance_first_cross = find_distance_to_first_crossed_wire(wire_1, wire_2)
    print('The distance to the first crossed wire is', distance_first_cross, 'when traveling through the wires')

