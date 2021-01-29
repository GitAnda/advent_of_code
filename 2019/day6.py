def get_dict_orbits(orbits):
    orbits_dict = {}
    for line in orbits:
        inner_object, outer_object = line.split(')')
        orbits_dict[outer_object] = inner_object

    return orbits_dict


def count_direct_and_indirect_orbits(orbits):
    orbits_dict = get_dict_orbits(orbits)

    count = 0
    for obj in orbits_dict.keys():
        sub_object = obj
        while sub_object != 'COM':
            sub_object = orbits_dict[sub_object]
            count += 1

    return count


def find_orbitted_objects(orbits, some_object):
    orbits_dict = get_dict_orbits(orbits)

    object_set = set()
    obj = some_object
    while obj != 'COM':
        obj = orbits_dict[obj]
        object_set.add(obj)

    return object_set


def count_orbits_between_objects(orbits, obj_1, obj_2):
    orbits_dict = get_dict_orbits(orbits)

    object_set_1 = find_orbitted_objects(orbits, obj_1)

    count = 0
    sub_object = obj_2
    while sub_object != 'COM':
        sub_object = orbits_dict[sub_object]
        count += 1
        if sub_object in object_set_1:
            last_shared_orbit = sub_object
            break

    obj = orbits_dict[obj_1]
    while obj != last_shared_orbit:
        obj = orbits_dict[obj]
        count += 1

    return count


if __name__ == '__main__':
    import sys

    f = open(sys.argv[1], 'r')
    orbits_list = f.read().split('\n')
    f.close()

    number_of_orbits = count_direct_and_indirect_orbits(orbits_list)
    print("The number of direct and indirect orbits is", number_of_orbits)
    number_of_orbits_between = count_orbits_between_objects(orbits_list, 'YOU', 'SAN')
    print("The number of orbits between YOU and SAN is", number_of_orbits_between)

