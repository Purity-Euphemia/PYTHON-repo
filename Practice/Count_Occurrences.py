game_board = [
    ['X', 'O', 'X'],
    ['O', 'X', ' '],
    [' ', 'O', 'X']
]

count_x = sum(row.count('X') for row in game_board)
count_o = sum(row.count('O') for row in game_board)
print("X count:", count_x)
print("O count:", count_o)
