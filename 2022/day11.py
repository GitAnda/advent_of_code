import input
import math
import copy
    
def parse_data():
    data = input.retrieve(__file__).split('\n\n')
    items = {}
    tests = {}
    for monkey in data:
        m, s, o, test, t, f = monkey.split('\n')
        m = int(m.split()[-1][:-1])
        s = [int(si) for si in s.split(': ')[-1].split(', ')]
        o = o.split(': ')[-1].split(' = ')[-1]
        test = int(test.split()[-1])
        t = int(t.split()[-1])
        f = int(f.split()[-1])
        items[m] = {"items": s, "inspects": 0}
        tests[m] = (o, test, t, f)

    return items, tests

initial_monkeys, TESTS = parse_data()
lcm = math.prod([test[1] for test in TESTS.values()])

def round(monkeys, relief):
    for m in monkeys:
        op, div, t, f = TESTS[m]
        for old in monkeys[m]["items"]:
            new = eval(op) // relief
            new = new % lcm
            if new % div == 0:
                monkeys[t]["items"].append(new)
            else:
                monkeys[f]["items"].append(new)
        monkeys[m]["inspects"] += len(monkeys[m]["items"])
        monkeys[m]["items"] = []
    return monkeys

def rounds(monkeys, n, relief):
    for i in range(n):
        monkeys = round(monkeys, relief)
    return monkeys

new_monkeys = rounds(copy.deepcopy(initial_monkeys), 20, 3)
a, b = sorted([new_monkeys[m]["inspects"] for m in new_monkeys], reverse=True)[:2]
res = a * b
print(f"Part 1: {res}")

new_monkeys = rounds(initial_monkeys, 10000, 1)
a, b = sorted([new_monkeys[m]["inspects"] for m in new_monkeys], reverse=True)[:2]
res = a * b
print(f"Part 2: {res}")
