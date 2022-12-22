import input
from functools import lru_cache
    
def parse_data():
    data = {}
    for line in input.retrieve(__file__).split('\n'):
        monkey, yell = line.split(': ')
        if yell.isnumeric():
            data[monkey] = int(yell)
        else:
            m1, op, m2 = yell.split()
            data[monkey] = (op, m1, m2)
    return data

DATA = parse_data()

@lru_cache(10000)
def yell(monkey):
    y = DATA[monkey]
    if isinstance(y, int):
        return y

    op, m1, m2 = y
    if op == "+":
        return yell(m1) + yell(m2)
    elif op == "-":
        return yell(m1) - yell(m2)
    elif op == "*":
        return yell(m1) * yell(m2)
    elif op == "/":
        return yell(m1) // yell(m2)
    
def yell_equal(monkey, value):
    if monkey == "humn":
        return value
    
    y = DATA[monkey]
    if isinstance(y, int):
        return y

    op, m1, m2 = y
    try:
        v1 = yell(m1)
        if op == "+":
            return yell_equal(m2, value - v1)
        elif op == "-":
            return yell_equal(m2, v1 - value)
        elif op == "*":
            return yell_equal(m2, value // v1)
        elif op == "/":
            return yell_equal(m2, v1 // value)
        
    except KeyError:
        v2 = yell(m2)
        if op == "+":
            return yell_equal(m1, value - v2)
        elif op == "-":
            return yell_equal(m1, v2 + value)
        elif op == "*":
            return yell_equal(m1, value // v2)
        elif op == "/":
            return yell_equal(m1, v2 * value)


res = yell("root")
print(f"Part 1: {res}")


yell.cache_clear()
DATA.pop("humn")
_, monkey1, monkey2 = DATA["root"]
value = yell(monkey2)
res = yell_equal(monkey1, value)
print(f"Part 2: {res}")
