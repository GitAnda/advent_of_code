from functools import lru_cache

file_name = 'day6.txt'

with open(file_name) as f:
    initial_fish = [int(x) for x in f.read().strip().split(',')]

freq_timer = {i: initial_fish.count(i) for i in range(7) if initial_fish.count(i) > 0}


@lru_cache()
def fish_made(internal_timer, days_left):
    if internal_timer >= days_left:
        return 0

    d = days_left - internal_timer - 1
    c = d // 7 + 1
    for i in range(c):
        c += fish_made(8, d - i * 7)

    return c


def count_fish(freq, days):
    count = 0
    for t, f in freq_timer.items():
        a = fish_made(t, days)
        count += (a + 1) * f
    return count


print(f'Part 1: {count_fish(freq_timer, 80)}')
print(f'Part 2: {count_fish(freq_timer, 256)}')