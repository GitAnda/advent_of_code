import aoc_input

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

numbers = [[c for c in line if c.isnumeric()] for line in data]

res = sum([int(n[0] + n[-1]) for n in numbers])
print(f"Part 1: {res}")

digit_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
digit_set = set(digit_map.keys()).union(digit_map.values())

def find_first_digit(line):
    for i in range(len(line)):
        for n in digit_set:
            if line[i:].startswith(n):
                if len(n) > 1:
                    return digit_map[n]
                return n
            
def find_last_digit(line):
    for i in range(len(line)):
        for n in digit_set:
            if line[:len(line)-i][::-1].startswith(n[::-1]):
                if len(n) > 1:
                    return digit_map[n]
                return n

res = sum([int(find_first_digit(line) + find_last_digit(line)) for line in data])
print(f"Part 2: {res}")    
        