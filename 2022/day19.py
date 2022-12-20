import input
import queue
# import regex as re
    
def parse_data():
    blueprints = {}
    for n, line in enumerate(input.retrieve(__file__).split('\n')):
        line = line.split()
        blueprints[n + 1] = (int(line[6]), int(line[12]), int(line[18]), int(line[21]), int(line[27]), int(line[30]))
    return blueprints

BLUEPRINTS = parse_data()

def max_geode(blueprint, start_time):
    crr, ccr, cor, coc, cgr, cgo = blueprint
    maxr, maxc, maxo = max(crr, ccr, cor, cgr), coc, cgo
    q = queue.Queue()
    q.put((start_time, (0, 0, 0, 0), (1, 0, 0, 0)))
    seen_states = set()
    
    best = 0
    while not q.empty():
        state = q.get()
        t, (mr, mc, mo, mg), (rr, rc, ro, rg) = state
        
        best = max(best, mg)
        if t == 0:
            continue
        
        # remove robots that we cannot spend
        rr, rc, ro = min(rr, maxr), min(rc, maxc), min(ro, maxo)
        # remove materials that we cannot spend
        mr, mc, mo = min(mr, maxr * t - rr * (t - 1)), min(mc, maxc * t - rc * (t - 1)), min(mo, maxo * t - ro * (t - 1))
        state = t, (mr, mc, mo, mg), (rr, rc, ro, rg)

        if state in seen_states:
            continue
        seen_states.add(state)
        
        q.put((t - 1, (mr + rr, mc + rc, mo + ro, mg + rg), (rr, rc, ro, rg)))
        if mr >= crr:
            q.put((t - 1, (mr + rr - crr, mc + rc, mo + ro, mg + rg), (rr + 1, rc, ro, rg)))
        if mr >= ccr:
            q.put((t - 1, (mr + rr - ccr, mc + rc, mo + ro, mg + rg), (rr, rc + 1, ro, rg)))
        if mr >= cor and mc >= coc:
            q.put((t - 1, (mr + rr - cor, mc + rc - coc, mo + ro, mg + rg), (rr, rc, ro + 1, rg)))
        if mr >= cgr and mo >= cgo:
            q.put((t - 1, (mr + rr - cgr, mc + rc, mo + ro - cgo, mg + rg), (rr, rc, ro, rg + 1)))
        
    return best

res = 0
for n, blueprint in BLUEPRINTS.items():  
    g = max_geode(blueprint, 24)
    res += n * g
print(f"Part 1: {res}")

res = 1
for n in range(1, 4):  
    blueprint = BLUEPRINTS[n]
    g = max_geode(blueprint, 32)
    res *= g
print(f"Part 2: {res}")
