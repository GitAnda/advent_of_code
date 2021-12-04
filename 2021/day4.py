file_name = 'day4.txt'

with open(file_name) as f:
    data = f.read().strip().split('\n\n')

numbers = [int(x) for x in data[0].split(',')]
boards = [[[int(x) for x in row.split()] for row in board.split('\n')] for board in data[1:]]

boards_turns = []

for board in boards:
    board_turns = []
    for row in board:
        row_turns = []
        for n in row:
            row_turns.append(numbers.index(n))
        board_turns.append(row_turns)
    boards_turns.append(board_turns)

boards_win_stat = []
for i, board in enumerate(boards_turns):
    win_turn = min([max(row) for row in board] + [max(column) for column in zip(*board)])
    boards_win_stat.append(win_turn)

min_win_turn = min(boards_win_stat)
win_board = boards_win_stat.index(min_win_turn)

sum_of_unmarked = 0
for i, row in enumerate(boards[win_board]):
    for j, n in enumerate(row):
        if boards_turns[win_board][i][j] > min_win_turn:
            sum_of_unmarked += n
win_value = numbers[min_win_turn]

print(f'Part 1: {sum_of_unmarked*win_value}')

max_win_turn = max(boards_win_stat)
win_board = boards_win_stat.index(max_win_turn)

sum_of_unmarked = 0
for i, row in enumerate(boards[win_board]):
    for j, n in enumerate(row):
        if boards_turns[win_board][i][j] > max_win_turn:
            sum_of_unmarked += n
win_value = numbers[max_win_turn]

print(f'Part 2: {sum_of_unmarked*win_value}')
