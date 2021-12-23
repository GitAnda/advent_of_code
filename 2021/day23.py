import queue
import numpy as np

#############
#...........#
###C#C#A#B###
  #D#D#B#A#
  #########

hallway = ['E'] * 7
room_a = ['C', 'D']
room_b = ['C', 'D']
room_c = ['A', 'B']
room_d = ['B', 'A']
# room_a = ['B', 'A']
# room_b = ['C', 'D']
# room_c = ['B', 'C']
# room_d = ['D', 'A']
state = ({'A': room_a, 'B': room_b, 'C': room_c, 'D': room_d}, hallway)
cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
room_location = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
N = 2


def move_out_of_room(current_state, room):
    new_locations = []
    _, hall = current_state
    for hall_loc in range(room_location[room], -1, -1):
        if hall[hall_loc] == 'E':
            new_locations.append(hall_loc)
        else:
            break
    for hall_loc in range(room_location[room]+1, 7):
        if hall[hall_loc] == 'E':
            new_locations.append(hall_loc)
        else:
            break
    return new_locations


def can_move_into_room(current_state, loc_in_hallway):
    _, hall = current_state
    amph = hall[loc_in_hallway]
    if len(rooms[amph]) > 0 and any(rooms[amph][i] != amph for i in range(len(rooms[amph]))):
        return False
    for hall_loc in range(loc_in_hallway + 1, room_location[amph] + 1):
        if hall[hall_loc] != 'E':
            return False
    for hall_loc in range(room_location[amph] + 1, loc_in_hallway):
        if hall[hall_loc] != 'E':
            return False
    return True


distance_matrix = {}
least_energy = np.inf
q = queue.LifoQueue()
# state = ({'A': ['B', 'A'], 'B': ['C', 'D'], 'C': ['C'], 'D': ['D', 'A']}, ['E', 'E', 'B', 'E', 'E', 'E', 'E'])  # 40
# state = ({'A': ['B', 'A'], 'B': ['D'], 'C': ['C'], 'D': ['D', 'A']}, ['E', 'E', 'B', 'C', 'E', 'E', 'E'])  # 200
# state = ({'A': ['B', 'A'], 'B': [], 'C': ['C', 'C'], 'D': ['D', 'A']}, ['E', 'E', 'B', 'D', 'E', 'E', 'E'])  # 3200
# state = ({'A': ['A'], 'B': ['B'], 'C': ['C', 'C'], 'D': ['D', 'A']}, ['E', 'E', 'B', 'D', 'E', 'E', 'E'])  # 50
# state = ({'A': ['A'], 'B': ['B', 'B'], 'C': ['C', 'C'], 'D': ['A']}, ['E', 'E', 'E', 'D', 'D', 'E', 'E'])  # 2020
# state = ({'A': ['A'], 'B': ['B', 'B'], 'C': ['C', 'C'], 'D': []}, ['E', 'E', 'E', 'D', 'D', 'A', 'E'])  # 3 + 7008
q.put((0, state))
while not q.empty():
    energy, state = q.get()
    (rooms, hallway) = state
    if energy >= least_energy:
        continue
    # print(energy, state)

    # move amphiods in hallway to rooms if possible
    while True:
        for loc in range(0, 7):
            if hallway[loc] != 'E' and can_move_into_room(state, loc):
                amphiod = hallway[loc]
                hallway[loc] = 'E'
                rooms[amphiod].append(amphiod)
                room_steps = N - len(rooms[amphiod])
                hallway_steps = max(loc - room_location[amphiod], room_location[amphiod] + 1 - loc) * 2
                if loc == 0 or loc == 6:
                    hallway_steps -= 1
                energy += (room_steps + hallway_steps) * cost[amphiod]
                break
        else:
            break

    # if all amphiods in their rooms record energy used
    if all([room.count(letter) == N for letter, room in rooms.items()]) and all([pos == 'E' for pos in hallway]):
        if energy < least_energy:
            print(f'finished with energy {energy}')
            least_energy = energy

    # move amphiods out of their rooms if there are any in the rooms
    for letter, room in rooms.items():
        if room and any(room[i] != letter for i in range(len(room))):
            amphiod = room[0]
            for new_loc in move_out_of_room(state, letter):
                new_rooms = {l: list(rooms[l]) for l in ['A', 'B', 'C', 'D']}
                new_rooms[letter] = room[1:]
                new_hallway = list(hallway)
                new_hallway[new_loc] = amphiod
                room_steps = N - len(room)
                hallway_steps = max(new_loc - room_location[letter], room_location[letter] + 1 - new_loc) * 2
                if new_loc == 0 or new_loc == 6:
                    hallway_steps -= 1
                new_energy = energy + (room_steps + hallway_steps) * cost[amphiod]
                # print((new_energy, (new_rooms, new_hallway)))
                q.put((new_energy, (new_rooms, new_hallway)))

print(f'Part 1: {least_energy}')



