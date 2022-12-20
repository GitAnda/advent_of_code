import input
from collections import defaultdict, deque
    
def parse_data():
    return [int(x) for x in input.retrieve(__file__).split('\n')]
    

class Node:
    def __init__(self, v, i):
        self.value = v
        self.next = None
        self.previous = None
        self.mixed = 0
        self.index = i
        self.rotate = v % 5000 if v % 5000 <= 2500 else v % 5000 - 5000
      
    def __repr__(self):
        return f"{self.previous.value}"
    
      
linkedlist = [Node(x, i) for i, x in enumerate(parse_data())]
for i, c in enumerate(linkedlist):
    n = linkedlist[(i + 1) % len(linkedlist)]
    p = linkedlist[i - 1]
    
    c.next = n
    c.previous = p    
    

def mix(linked):
    current_node = linked[0]
    
    while count < len(linked):
        next_node = current_node
        
        r = 0
        while r != current_node.rotate:
            next_prev = 
        
        count += 1
        
        # print(n)

res = mix(CODE)
print(f"Part 1: {res}")

res = 0
print(f"Part 2: {res}")
