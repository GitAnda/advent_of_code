file_name = 'day14.txt'
with open(file_name) as f:
    initial_string, inserts = f.read().strip().split('\n\n')
inserts = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in inserts.split('\n')}
string = initial_string

pairs = {k: 0 for k in inserts.keys()}
for i in range(len(initial_string)-1):
    pairs[initial_string[i:i+2]] += 1


def step(pairs):
    add_pairs = {k: 0 for k in inserts.keys()}
    for p, n in pairs.items():
        i = inserts[p]
        add_pairs[p[0] + i] += n
        add_pairs[i + p[1]] += n
    return add_pairs


def get_score(pairs):
    counts = {k: 0 for k in set(inserts.values())}
    counts[initial_string[0]] += 1
    counts[initial_string[-1]] += 1
    for p, n in pairs.items():
        counts[p[0]] += n
        counts[p[1]] += n
    sorted_counts = sorted(counts.values())
    return int((sorted_counts[-1]-sorted_counts[0])/2)


for i in range(40):
    pairs = step(pairs)
    if i == 9:
        print(f'Part 1: {get_score(pairs)}')
print(f'Part 2: {get_score(pairs)}')

