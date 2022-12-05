import input
    
def parse_data():
    crates, moves = input.retrieve(__file__).split('\n\n')
    crates = [[crate[c] for c in range(1, len(crate), 4)] for crate in crates.split('\n')]
    crates = [list(filter(lambda a: a != ' ', list(stack)[::-1])) for stack in zip(*crates[:-1])]
    moves = [(int(move.split()[1]), int(move.split()[3]) - 1, int(move.split()[5]) - 1) for move in moves.split('\n')]
    return crates, moves

crates, moves = parse_data()

def do_move(move, crates, reverse=False):
    n, f, t = move
    
    crate = crates[f][-n:]
    if reverse:
        crate = list(reversed(crate))
        
    crates[f] = crates[f][:-n]
    crates[t] =  crates[t] + crate
    return crates

new_crates = [crate.copy() for crate in crates]
for move in moves:
    new_crates = do_move(move, new_crates, reverse=True)
res = ''.join([stack[-1] for stack in new_crates])
print(f"Part 1: {res}")

new_crates = [crate.copy() for crate in crates]
for move in moves:
    new_crates = do_move(move, new_crates, reverse=False)
res = ''.join([stack[-1] for stack in new_crates])
print(f"Part 2: {res}")