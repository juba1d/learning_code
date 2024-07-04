def king_moves(start, end):
    # Converting chessboard coordinates to numeric values
    column_start, row_start = ord(start[0]) - ord('a') + 1, int(start[1])
    column_end, row_end = ord(end[0]) - ord('a') + 1, int(end[1])

    moves = []
    
    while column_start != column_end or row_start != row_end:
        move = ""
        if column_start < column_end:
            move += "R"
            column_start += 1
        elif column_start > column_end:
            move += "L"
            column_start -= 1
        
        if row_start < row_end:
            move += "U"
            row_start += 1
        elif row_start > row_end:
            move += "D"
            row_start -= 1
        
        moves.append(move)

    return len(moves), moves

# Input coordinates
start_square = input().strip()
end_square = input().strip()

# Get the minimum number of moves and the moves themselves
number_of_moves, moves_list = king_moves(start_square, end_square)

# Output the result
print(number_of_moves)
for move in moves_list:
    print(move)
