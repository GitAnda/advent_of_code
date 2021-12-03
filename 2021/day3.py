file_name = 'day3.txt'

with open(file_name) as f:
    bits = f.read().strip().split()


def find_number_of_ones(bits):
    res = [0]*len(bits[0])
    for bit in bits:
        for i, b in enumerate(bit):
            res[i] += int(b)
    return res


def bit_to_int(bit):
    return sum([b*pow(2, len(bit)-i-1) for i, b in enumerate(bit)])


gamma = [round(r/len(bits)) for r in find_number_of_ones(bits)]
epsilon = [1-g for g in gamma]

print(f'Part 1: {bit_to_int(gamma)*bit_to_int(epsilon)}')

with open(file_name) as f:
    bits_left = f.read().strip().split()
idx = 0
while len(bits_left) > 1:
    one_freq = find_number_of_ones(bits_left)[idx]
    if one_freq >= len(bits_left)/2:
        most_common_bit = 1
    else:
        most_common_bit = 0
    bits_left = [bit for bit in bits_left if int(bit[idx]) == most_common_bit]
    idx += 1
oxygen = [int(x) for x in bits_left[0]]
print(oxygen)

with open(file_name) as f:
    bits_left = f.read().strip().split()
idx = 0
while len(bits_left) > 1:
    one_freq = find_number_of_ones(bits_left)[idx]
    if one_freq >= len(bits_left) / 2:
        most_common_bit = 0
    else:
        most_common_bit = 1
    bits_left = [bit for bit in bits_left if int(bit[idx]) == most_common_bit]
    idx += 1
co2 = [int(x) for x in bits_left[0]]
print(co2)

print(f'Part 2: {bit_to_int(oxygen)*bit_to_int(co2)}')
