import input
import textwrap
    
def parse_data():
    data = input.retrieve(__file__).split('\n')
    return data


def get_register_data(instrs):
    register = [1, 1]
    for instr in instrs:
        register.append(register[-1])
        if not instr.startswith("noop"):
            n = int(instr.split()[1].strip())
            register.append(register[-1] + n)

    return register

def draw(regs):
    CRT = []
    list(range(1, 41)) * 6
    for sprite, c in zip(regs, list(range(1, 41)) * 6):
        # print(sprite, c)
        if sprite <= c and c < sprite + 3:
            CRT.append("#")
        else:
            CRT.append(".")
    CRT = textwrap.wrap(''.join(CRT), 40)
    for c in CRT:
        print(c)


data = parse_data()
register = get_register_data(data)

res = sum([i * d for i, d in enumerate(register) if i % 20 == 0][1::2])
print(f"Part 1: {res}")

print(f"Part 2: ")
draw(register[1:])
