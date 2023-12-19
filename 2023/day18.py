import aoc_input
from queue import Queue

day = int(__file__[-5:-3])
data = aoc_input.get(day).strip().split("\n")

# def calculate_internal_slow():
#     edges = {(0, 0)}
#     pos = (0, 0)

#     for d in data:
#         direction, length, _ = d.strip().split(" ")
#         length = int(length)

#         match direction:
#             case "U":
#                 di, dj = (-1, 0)
#             case "D":
#                 di, dj = (1, 0)
#             case "L":
#                 di, dj = (0, -1)
#             case "R":
#                 di, dj = (0, 1)

#         i, j = pos
#         for l in range(length):
#             edges.add((i + l * di, j + l * dj))
#         pos = (i + length * di, j + length * dj)

#     MAX_I, MAX_J = 0, 0
#     MIN_I, MIN_J = float("inf"), float("inf")
#     for e in edges:
#         i, j = e
#         if i > MAX_I:
#             MAX_I = i
#         if j > MAX_J:
#             MAX_J = j
#         if i < MIN_I:
#             MIN_I = i
#         if j < MIN_J:
#             MIN_J = j

#     q = Queue()
#     q.put((MIN_I + (MAX_I - MIN_I) // 2, MIN_J + (MAX_J - MIN_J) // 2))
#     while not q.empty():
#         i, j = q.get()
#         if (i, j) in edges:
#             continue

#         edges.add((i, j))
#         neighbours = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
#         for n in neighbours:
#             if not n in edges:
#                 q.put(n)

#     for i in range(MIN_I, MAX_I+1):
#         line = f"{i:02d} "
#         for j in range(MIN_J, MAX_J+1):
#             if (i, j) in edges:
#                 line += "#"
#             elif (i, j) == (MIN_I + (MAX_I - MIN_I) // 2, MIN_J + (MAX_J - MIN_J) // 2):
#                 line += "X"
#             else:
#                 line += " "
#         print(line)
#     print()

#     return len(edges)

# res = calculate_internal_slow()
# print(f"Part 1: {res}")

def get_sorted_corners(data, simple=True):
    corners = {(0, 0)}
    pos = (0, 0)

    for d in data:
        if simple:
            direction, length, _ = d.strip().split(" ")
            length = int(length)
        else:
            _, _, color = d.strip().split(" ")
            length, direction = color[2:7], color[-2]
            length = int(length, base=16)

        match direction:
            case "U":
                di, dj = (-1, 0)
            case "D":
                di, dj = (1, 0)
            case "L":
                di, dj = (0, -1)
            case "R":
                di, dj = (0, 1)
            case "3":
                di, dj = (-1, 0)
            case "1":
                di, dj = (1, 0)
            case "2":
                di, dj = (0, -1)
            case "0":
                di, dj = (0, 1)

        i, j = pos
        pos = (i + length * di, j + length * dj)
        corners.add(pos)

    # Get 
    # MAX_I, MAX_J = 0, 0
    # MIN_I, MIN_J = float("inf"), float("inf")
    # for e in corners:
    #     i, j = e
    #     if i > MAX_I:
    #         MAX_I = i
    #     if j > MAX_J:
    #         MAX_J = j
    #     if i < MIN_I:
    #         MIN_I = i
    #     if j < MIN_J:
    #         MIN_J = j
            
    sorted_corners = {}
    px = None
    for xy in sorted(corners):
        if px is None:
            sublist = [xy[1]]
        elif xy[0] != px:
            sorted_corners[px] = sublist
            sublist = [xy[1]]
        else:
            sublist.append(xy[1])
        px = xy[0]
    sorted_corners[px] = sublist

    for key, item in sorted_corners.items():
        sorted_corners[key] = [(item[i], item[i+1]) for i in range(0, len(item), 2)]
    print(sorted_corners)

def calculate_internal(corners):
    

    # for i in range(MIN_I, MAX_I+1):
    #     line = f"{i:02d} "
    #     for j in range(MIN_J, MAX_J+1):
    #         if (i, j) in corners:
    #             line += "#"
    #         # elif (i, j) == (MIN_I + (MAX_I - MIN_I) // 2, MIN_J + (MAX_J - MIN_J) // 2):
    #         #     line += "X"
    #         else:
    #             line += " "
    #     print(line)
    # print()

    res = 0

    widths = []
    current_x = None
    for new_x, intervals in sorted_corners.items():
        new_widths = []
        considered_intervals = set()

        for width in widths:
            w0, w1 = width
            new_w0, new_w1 = None, None
            height = new_x - current_x

            for interval in intervals:
                y0, y1 = interval
                
                # End of the interval.
                if y0 == w0 and y1 == w1:
                    res += (y1 - y0 + 1) * height
                    considered_intervals.add(interval)
                    break
                
                # Interval splits a width
                if y0 > w0 and y1 < w1:
                    res += (w1 - w0 + 1) * (height - 1)
                    # res += y0 - w0 + 1 + w1 - y1 + 1
                    res += w1 - w0 + 1
                    new_widths.append((w0, y0))
                    new_widths.append((y1, w1))
                    considered_intervals.add(interval)
                    break

                temp = move_interval(interval, w0)
                if temp is not None:
                    new_w0 = temp
                    considered_intervals.add(interval)

                temp = move_interval(interval, w1)
                if temp is not None:
                    new_w1 = temp
                    considered_intervals.add(interval)
                
            else:
                # Both coordinatese of the interval move
                if new_w0 is not None and new_w1 is not None:
                    new_widths.append((new_w0, new_w1))
                    min_w0 = min(new_w0, w0)
                    max_w1 = max(new_w1, w1)
                
                # First coordinate of the interval moves
                elif new_w0 is not None:
                    new_widths.append((new_w0, w1))
                    min_w0 = min(new_w0, w0)
                    max_w1 = w1
                
                # Second coordinate of the interval moves
                elif new_w1 is not None:
                    new_widths.append((w0, new_w1))
                    min_w0 = w0
                    max_w1 = max(new_w1, w1)
                
                else:
                    new_widths.append((w0, w1))
                    min_w0 = w0
                    max_w1 = w1

                res += (w1 - w0 + 1) * (height - 1)
                res += max_w1 - min_w0 + 1

        # New intervals should be added
        for interval in intervals:
            y0, y1 = interval
            if interval not in considered_intervals:
                res += (y1 - y0 + 1)
                new_widths.append((y0, y1))

        widths = new_widths
        current_x = new_x
    
    return res



def move_interval(interval, y):
    if y == interval[0]:
        return interval[1]
    if y == interval[1]:
        return interval[0]
    return None
        

    

    return len(corners)

res = calculate_internal()
print(f"Part 2: {res}")

# edges = {(0, 0)}
# pos = (0, 0)

# for d in data:
#     _, _, color = d.strip().split(" ")
#     length, direction = color[2:7], color[-2]
#     length = int(length, base=16)

#     match direction:
#         case "3":
#             di, dj = (-1, 0)
#         case "1":
#             di, dj = (1, 0)
#         case "2":
#             di, dj = (0, -1)
#         case "0":
#             di, dj = (0, 1)

#     i, j = pos
#     for l in range(length):
#         edges.add((i + l * di, j + l * dj))
#     pos = (i + length * di, j + length * dj)

# MAX_I, MAX_J = 0, 0
# MIN_I, MIN_J = float("inf"), float("inf")
# for e in edges:
#     i, j = e
#     if i > MAX_I:
#         MAX_I = i
#     if j > MAX_J:
#         MAX_J = j
#     if i < MIN_I:
#         MIN_I = i
#     if j < MIN_J:
#         MIN_J = j

# q = Queue()
# q.put((MIN_I + (MAX_I - MIN_I) // 2, MIN_J + (MAX_J - MIN_J) // 2))
# while not q.empty():
#     i, j = q.get()
#     if (i, j) in edges:
#         continue

#     edges.add((i, j))
#     neighbours = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
#     for n in neighbours:
#         if not n in edges:
#             q.put(n)

# res = 0
# print(f"Part 2: {res}")
        