import input
# import queue
# from functools import lru_cache
# import math

def parse_data():
    data = input.retrieve(__file__).split('\n')
    return data

CONV = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
ADD = {'=': {'=': ('-', '1'), '-': ('-', '2'), '0': ('0', '='), '1': ('0', '-'), '2': ('0', '0')},
       '-': {'=': ('-', '2'), '-': ('0', '='), '0': ('0', '-'), '1': ('0', '0'), '2': ('0', '1')},
       '0': {'=': ('0', '='), '-': ('0', '-'), '0': ('0', '0'), '1': ('0', '1'), '2': ('0', '2')},
       '1': {'=': ('0', '-'), '-': ('0', '0'), '0': ('0', '1'), '1': ('0', '2'), '2': ('1', '=')},
       '2': {'=': ('0', '0'), '-': ('0', '1'), '0': ('0', '2'), '1': ('1', '='), '2': ('1', '-')}}

def add_with_carry(snafu1, snafu2, carry):
    c1, s1 = ADD[snafu1][snafu2]
    c2, s2 = ADD[s1][carry]
    d, c3 = ADD[c1][c2]
    if d != '0':
       print(f"Problems with {(snafu1, snafu2, carry)}")
    return c3, s2

def add_snafu(snafu1, snafu2):
    l = max(len(snafu1), len(snafu2)) + 1
    snafu1, snafu2 = snafu1.zfill(l), snafu2.zfill(l)
    carry = '0'
    sum_snafu = ''
    for s1, s2 in zip(snafu1[::-1], snafu2[::-1]):
        carry, s = add_with_carry(s1, s2, carry)
        sum_snafu += s
    return sum_snafu[::-1].lstrip('0')
        
data = parse_data()
res = ''
for snafu in data:
    res = add_snafu(res, snafu)
print(f"Part 1: {res}")



