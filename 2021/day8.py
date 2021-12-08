file_name = 'day8.txt'

with open(file_name) as f:
    signals, digits = list(zip(*[x.split(' | ') for x in f.read().strip().split('\n')]))

digits = [x.split(' ') for x in digits]
signals = [x.split(' ') for x in signals]
unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}

res = 0
for line in digits:
    for d in line:
        if len(d) in unique_lengths.keys():
            res += 1

print(f'Part 1: {res}')

final_digits = 0
for signal, digit in zip(signals, digits):
    res = {}
    len_five = []
    len_six = []
    for d in signal:
        if len(d) in unique_lengths:
            res[unique_lengths[len(d)]] = set(d)
        elif len(d) == 5:
            len_five.append(set(d))
        else:
            len_six.append(set(d))

    int_five = set.intersection(*len_five)
    for d in len_five:
        if d.difference(int_five) == res[1]:
            res[3] = d
        elif d.difference(int_five).issubset(res[4]):
            res[5] = d
        else:
            res[2] = d

    for d in len_six:
        if res[3].issubset(d):
            res[9] = d
        elif res[5].issubset(d):
            res[6] = d
        else:
            res[0] = d


    res = {''.join(sorted(list(item))): key for key, item in res.items()}

    final_digits += int(''.join([str(res[''.join(sorted(s))]) for s in digit]))

print(f'Part 2: {final_digits}')
