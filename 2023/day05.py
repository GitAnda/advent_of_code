import aoc_input

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip()

def get_map(data):
    lines = data.split("\n")
    names = lines[0].split("-")
    src, dst = names[0], names[2]

    lines = lines[1:]
    convert = []
    for line in lines:
        convert.append(tuple([int(l) for l in line.split(" ")]))

    return src, dst, convert


raw_maps = data.split("\n\n")
seeds = [int(s) for s in raw_maps[0].split(": ")[1].split(" ")]

for m in raw_maps[1:]:
    _, _, values = get_map(m)

    for i, seed in enumerate(seeds):

        for dst_start, src_start, src_len in values:
            if src_start <= seed < src_start + src_len:
                seeds[i] = dst_start + (seed - src_start)
                break

res = min(seeds)
print(f"Part 1: {res}")

values = [int(s) for s in raw_maps[0].split(": ")[1].split(" ")]
seeds = [(values[i], values[i+1]) for i in range(0, len(seeds), 2)]

for m in raw_maps[1:]:
    _, _, values = get_map(m)
    print(seeds)
    new_seeds = []

    for seed_start, seed_len in seeds:
        seed_end = seed_start + seed_len - 1
        mapped_seeds = []

        for dst_start, src_start, src_len in values:
            src_end = src_start + src_len - 1
            dst_end = dst_start + src_len - 1

            # intervals do not overlap
            if seed_end < src_start:
                continue
            if src_end < seed_start:
                continue
            
            # Seed interval wholly contained in mapped interval
            if src_start <= seed_start and src_end >= seed_end:
                new_seeds.append((dst_start + seed_start - src_start, seed_len))
                # print(new_seeds[-1])
                mapped_seeds.append((seed_start, seed_end))
                break

            # Seed interval wholly contains mapped interval
            elif src_start >= seed_start and src_end <= seed_end:
                new_seeds.append((dst_start, src_len))
                # print(new_seeds[-1])
                mapped_seeds.append((src_start, src_end))
            
            # Source interval right overlap with mapped interval
            elif src_start < seed_start and seed_start <= src_end:
                new_seeds.append((dst_start + seed_start - src_start, src_end - seed_start + 1))
                # print(new_seeds[-1])
                mapped_seeds.append((seed_start, src_end))

            # Source interval left overlap with mapped interval
            elif src_start <= seed_end and src_end > seed_end:
                new_seeds.append((dst_start, seed_end - src_start + 1))
                # print(new_seeds[-1])
                mapped_seeds.append((src_start, seed_end))

            else:
                raise Exception("Something has gone horribly wrong...")
            
        mapped_seeds = sorted(mapped_seeds)
        if not mapped_seeds:
            new_seeds.append((seed_start, seed_len))
            # print(new_seeds[-1])
            continue
        
        if mapped_seeds[0][0] > seed_start:
            new_seeds.append((seed_start, mapped_seeds[0][0] - seed_start))
            # print(new_seeds[-1])
        if mapped_seeds[-1][-1] < seed_end:
            new_seeds.append((mapped_seeds[-1][1] + 1, seed_end - mapped_seeds[-1][1]))
            # print(new_seeds[-1])

        for interval1, interval2 in zip(mapped_seeds, mapped_seeds[1:]):
            if interval2[0] - interval1[1] > 1:
                new_seeds.append((interval1[1] + 1, interval2[0] - interval1[1] - 1))
                # print(new_seeds[-1])

    seeds = new_seeds

print(seeds)
res = min([seed[0] for seed in seeds])
print(f"Part 2: {res}")    
        