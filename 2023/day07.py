import aoc_input
import re
from functools import cmp_to_key

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

CARDS = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

bids = {}
for d in data:
    hand, bid = re.findall("(.{5}) (\d+)", d)[0]
    bids[hand] = int(bid)

def get_type(hand):
    t = {h: hand.count(h) for h in hand}
    match sorted(t.values(), reverse=True):
        case (5, ):
            return 7
        case (4, 1):
            return 6
        case (3, 2):
            return 5
        case (3, 1, 1):
            return 4
        case (2, 2, 1):
            return 3
        case (2, 1, 1, 1):
            return 2
        case (1, 1, 1, 1, 1):
            return 1
    
    x = "What?"
    
def compare_hand(hand1, hand2):
    type1 = get_type(hand1)
    type2 = get_type(hand2)

    if type1 > type2:
        return 1
    if type1 < type2:
        return -1
    
    for c1, c2 in zip(hand1, hand2):
        if CARDS[c1] > CARDS[c2]:
            return 1
        if CARDS[c1] < CARDS[c2]:
            return -1
        
    return 0

sorted_hands = sorted(bids.keys(), key=cmp_to_key(compare_hand))
res = sum(bids[h] * (i + 1) for i, h in enumerate(sorted_hands))
print(f"Part 1: {res}")

CARDS = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def get_type(hand):
    if hand == "JJJJJ":
        return 7
    
    t = {h: hand.count(h) for h in hand}

    if 'J' in t:
        c = t['J']
        del t['J']
        count_t = sorted(t.values(), reverse=True)
        count_t[0] += c
    else:
        count_t = sorted(t.values(), reverse=True)

    match count_t:
        case (5, ):
            return 7
        case (4, 1):
            return 6
        case (3, 2):
            return 5
        case (3, 1, 1):
            return 4
        case (2, 2, 1):
            return 3
        case (2, 1, 1, 1):
            return 2
        case (1, 1, 1, 1, 1):
            return 1
    
    x = "What?"
    
def compare_hand(hand1, hand2):
    type1 = get_type(hand1)
    type2 = get_type(hand2)

    if type1 > type2:
        return 1
    if type1 < type2:
        return -1
    
    for c1, c2 in zip(hand1, hand2):
        if CARDS[c1] > CARDS[c2]:
            return 1
        if CARDS[c1] < CARDS[c2]:
            return -1
        
    return 0

sorted_hands = sorted(bids.keys(), key=cmp_to_key(compare_hand))
res = sum(bids[h] * (i + 1) for i, h in enumerate(sorted_hands))
print(f"Part 2: {res}")    
        