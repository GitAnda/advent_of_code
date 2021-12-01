from functools import lru_cache


class CardDeck:
    def __init__(self, n):
        self.deck = list(range(n))
        self.len = n
        with open("day22.txt") as f:
            self.technique_list = [x for x in f.read().strip().split('\n')]

    def do_technique(self, technique_string):
        if technique_string == 'deal into new stack':
            self.deal_into_new_stack()
        elif 'cut' in technique_string:
            n = int(technique_string[4:]) % self.len
            self.cut_cards(n)
        else:
            n = int(technique_string[20:])
            self.deal_with_increment(n)

    def deal_into_new_stack(self):
        self.deck.reverse()

    def cut_cards(self, n):
        self.deck = self.deck[n:] + self.deck[:n]

    def deal_with_increment(self, n):
        new_deck = [0]*self.len
        for current_pos in range(self.len):
            new_pos = (n * current_pos) % self.len
            new_deck[new_pos] = self.deck[current_pos]
        self.deck = new_deck

    def deal(self):
        for i, technique in enumerate(self.technique_list):
            # print(self.deck)
            self.do_technique(technique)
        # print(self.deck)

    def find_card(self, n):
        for i in range(self.len):
            if self.deck[i] == n:
                return i


class CardDeckReverse:
    def __init__(self, n, end_pos):
        self.len = n
        self.pos = end_pos
        with open("day22.txt") as f:
            self.technique_list = reversed([x for x in f.read().strip().split('\n')])

    def do_technique(self, technique_string):
        if technique_string == 'deal into new stack':
            self.deal_into_new_stack()
        elif 'cut' in technique_string:
            n = int(technique_string[4:]) % self.len
            self.cut_cards(n)
        else:
            n = int(technique_string[20:])
            self.deal_with_increment(n)

    def deal_into_new_stack(self):
        self.pos = self.len - self.pos - 1

    def cut_cards(self, n):
        if self.len - self.pos > n:
            self.pos = self.pos + n
        else:
            self.pos = self.pos - self.len + n

    def deal_with_increment(self, n):
        # old_pos = self.pos
        # pos = self.pos
        # while True:
        #     new_pos = (n * pos) % self.len
        #     print(new_pos)
        #     if new_pos == old_pos:
        #         self.pos = pos
        #     else:
        #         pos = new_pos

        c = modinv(self.len % n, n) * (- self.pos) % n
        self.pos = (self.pos + c * self.len) // n

    def deal(self):
        for i, technique in enumerate(self.technique_list):
            self.do_technique(technique)

    def get_starting_pos(self, n):
        for x in range(n):
            if x % 1000000 == 0:
                print(f'{x} ({round(x/n*100)})% : {self.pos}', end="\r")
            for i, technique in enumerate(self.technique_list):
                # print('test', self.pos)
                self.do_technique(technique)

        return self.pos


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


if __name__ == '__main__':
    print('part 1:', end=' ')
    cards = CardDeck(10007)
    cards.deal()
    print(cards.find_card(2019))
    # print('\npart 2:')
    # cards = CardDeckReverse(119315717514047, 2020)
    # print(cards.get_starting_pos(101741582076661))

    # cards = CardDeck(10)
    # cards.deal()
    # r_cards = CardDeckReverse(10, 8)
    # print(r_cards.get_starting_pos(1))