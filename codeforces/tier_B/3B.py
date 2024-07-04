def check_winner(board, player):
    win_positions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    
    for pos in win_positions:
        if all(board[r][c] == player for r, c in pos):
            return True
    return False

def tic_tac_toe_result(board):
    count_X = sum(row.count('X') for row in board)
    count_O = sum(row.count('0') for row in board)
    
    if not (count_X == count_O or count_X == count_O + 1):
        return "illegal"
    
    first_won = check_winner(board, 'X')
    second_won = check_winner(board, '0')
    
    if first_won and second_won:
        return "illegal"
    if first_won and count_X == count_O + 1:
        return "the first player won"
    if second_won and count_X == count_O:
        return "the second player won"
    if first_won or second_won:
        return "illegal"
    if count_X + count_O == 9:
        return "draw"
    if count_X == count_O:
        return "first"
    return "second"

# Input reading
board = [input().strip() for _ in range(3)]

# Determine the result
result = tic_tac_toe_result(board)

# Output the result
print(result)

