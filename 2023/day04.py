import aoc_input

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

cards = {}
for line in data:
    card, numbers = line.split(": ")
    card = card[5:].strip()
    win, have = numbers.split(" | ")
    win = [int(n) for n in win.split(" ") if n]
    have = [int(n) for n in have.split(" ") if n]
    
    cards[card] = (win, have)

total_cards = len(cards)

def calcualte_points(win, have):
    count = 0
    for w in win:
        if w in have:
            count += 1

    return count

total_points = 0
num_instances = {str(i + 1): 1 for i in range(len(data))}
for card, (win, have) in cards.items():
    count = calcualte_points(win, have)
    total_points += 2 ** (count - 1) if count > 0 else 0

    for card_number in range(int(card) + 1, min(int(card) + count + 1, total_cards + 1)):
        num_instances[str(card_number)] += num_instances[card]


res = total_points
print(f"Part 1: {res}")

res = sum(num_instances.values())
print(f"Part 2: {res}")    
        