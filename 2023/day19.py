import aoc_input
from queue import Queue
import re

day = int(__file__[-5:-3])
WORKFLOWS, PARTS = aoc_input.get(day).strip().split("\n\n")
WORKFLOWS = {re.findall("(.+){(.+)}", workflow)[0][0]: re.findall("(.+){(.+)}", workflow)[0][1].split(",") for workflow in WORKFLOWS.split("\n")}
PARTS = [[int(d) for d in re.findall("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", part)[0]] for part in PARTS.split("\n")]
PARTS = [{"x": part[0], "m": part[1], "a": part[2], "s": part[3]} for part in PARTS]

def follow_workflows(part):
    workflow = "in"
    while True:
        if workflow == "A":
            return True
        if workflow == "R":
            return False

        steps = WORKFLOWS[workflow]
        for step in steps:
            if not ":" in step:
                workflow = step
                break
            
            equation, next_workflow = step.split(":")
            x,m,a,s = part.values()
            if eval(equation):
                workflow = next_workflow
                break

# print(WORKFLOWS)
# print(PARTS)

res = 0
for part in PARTS:
    if follow_workflows(part):
        res += sum(part.values())

print(f"Part 1: {res}")

def get_number(part):
    prod = 1
    for p in "xmas":
        l, u = part[p]
        prod *= u - l + 1
    return prod

res = 0
q = Queue()
q.put(("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}))
while not q.empty():
    workflow, part = q.get()
    if workflow == "A":
        res += get_number(part)
        continue
    if workflow == "R":
        continue

    steps = WORKFLOWS[workflow]
    for step in steps:
        if not ":" in step:
            q.put((step, dict(part)))
            break

        equation, next_workflow = step.split(":")
        xmas, sign, num = equation[0], equation[1], int(equation[2:])
        if sign == "<":
            l, u = part[xmas]
            if l < num:
                new_part = dict(part)
                new_part[xmas] = (l, min(num - 1, u))
                q.put((next_workflow, new_part))

            if u >= num:
                part[xmas] = (max(num, l), u)
            else:
                break

        if sign == ">":
            l, u = part[xmas]
            if u > num:
                new_part = dict(part)
                new_part[xmas] = (max(l, num + 1), u)
                q.put((next_workflow, new_part))

            if l <= num:
                part[xmas] = (l, min(num, u))
            else:
                break

print(f"Part 2: {res}")