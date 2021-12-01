# For this question I have manually created the graph with distances and depths.
# (This was done using the maze pruning code from part 1)
#
#              AA
#               | 3
#       -------(s)-------
#  241 |  <-3       <-5  | 329
#      |        54       |
#     (c0)--------------(c1)
#      |                 |
#  800 |  <-12      <-7  | 393
#       -------(t)-------
#               | 1
#              ZZ

if __name__ == '__main__':
    import queue

    graph = {
        's': {'c0': (241, 3), 'c1': (329, -5)},
        'c0': {'s': (241, -3), 'c1': (54, 0), 't': (800, -12)},
        'c1': {'s': (329, 5), 'c0': (54, 0), 't': (393, 7)},
        't': {'c0': (800, 12), 'c1': (393, -7)}
    }

    start = ('s', 0, 0)  # (node, dist, depth)
    end = ('t', 0, 0)
    dist_matrix = {('s', 0): 0}  # (node, depth): dist
    max_depth = 200

    q = queue.Queue()
    q.put(start)
    while not q.empty():
        node, dist, depth = q.get()
        neighbours = graph[node]
        for new_node, (d_dist, d_depth) in neighbours.items():
            if 0 <= depth + d_depth <= 200:
                new_depth = depth + d_depth
                new_dist = dist + d_dist
                if (new_node, new_depth) not in dist_matrix or new_dist < dist_matrix[(new_node, new_depth)]:
                    q.put((new_node, new_dist, new_depth))
                    dist_matrix[(new_node, new_depth)] = new_dist

                if new_node == 't' and new_depth == 0:
                    print(new_dist+4)
                    break

        else:
            continue
        break






