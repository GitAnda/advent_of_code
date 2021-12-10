import queue

file_name = 'day10.txt'

with open(file_name) as f:
    code = f.read().strip().split('\n')

pairs = {')': '(', '}': '{', '>': '<', ']': '['}
inv_pairs = {v: k for k, v in pairs.items()}
corrupted_points = {')': 3, '}': 1197, '>': 25137, ']': 57}
autocorrect_points = {')': 1, '}': 3, '>': 4, ']': 2}
openings = set(pairs.values())

corrupted_score = 0
autocorrect_scores = []
for line in code:
    q = queue.LifoQueue()
    corrupted = False
    for char in line:
        if char in openings:
            q.put(char)
        else:
            e = q.get()
            if pairs[char] != e:
                corrupted_score += corrupted_points[char]
                corrupted = True

    if not corrupted:
        autocorrect_score = 0
        while not q.empty():
            e = q.get()
            autocorrect_score *= 5
            autocorrect_score += autocorrect_points[inv_pairs[e]]
        autocorrect_scores.append(autocorrect_score)

print(f'Part 1: {corrupted_score}')

autocorrect_scores = sorted(autocorrect_scores)
n = len(autocorrect_scores)

print(f'Part 2: {autocorrect_scores[n//2]}')
