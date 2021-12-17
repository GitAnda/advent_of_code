import numpy as np

xt = (211, 232)
yt = (-124, -69)

# xt = (20, 30)
# yt = (-10, -5)


def y_ends_in_target(vs, target):
    pos = 0
    count = 0
    res = []
    b = False
    while True:
        pos += vs
        vs -= 1
        if target[0] <= pos <= target[1]:
            res.append(count+1)
            b = True
        elif pos < target[0]:
            break
        count += 1
    return b, res


def x_ends_in_target(target, time_steps):
    min_vs = int(np.ceil(np.sqrt(target[0]*2+0.25)-0.5))
    max_vs = target[1]
    res = []
    b = False
    for vs in range(min_vs, max_vs+1):
        pos = 0
        v = vs
        for _ in range(time_steps):
            pos += v
            v = max(0, v - 1)
            if v == 0:
                break

        if target[0] <= pos <= target[1]:
            res.append(vs)
            b = True
        elif pos > target[1]:
            break

    return b, res


def get_highest_y(all_scores):
    max_y = 0
    for _, y in all_scores:
        if y > max_y:
            max_y = y
    return max_y*(max_y+1)//2


def get_all_scores(xt, yt):
    res = []
    vy = abs(yt[0]) - 1
    while vy >= yt[0]:
        y_score, times = y_ends_in_target(vy, yt)
        if y_score:
            for t in times:
                x_score, vxs = x_ends_in_target(xt, t)
                if x_score:
                    for vx in vxs:
                        res.append((vx, vy))
        vy -= 1
    return res


all_scores = get_all_scores(xt, yt)
print(f'Part 1: {get_highest_y(all_scores)}')
print(f'Part 2: {len(set(all_scores))}')

