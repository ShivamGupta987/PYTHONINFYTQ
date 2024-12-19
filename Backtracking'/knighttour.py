# Initialize a matrix with -1
def is_safe(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

# Try all next moves for the knight
def knight_tour(x, y, move_count, board, move_x, move_y, N):
    # If all squares are visited
    if move_count == N * N:
        return True
    
    # Try all possible moves for a knight
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        
        if is_safe(next_x, next_y, board, N):
            board[next_x][next_y] = move_count
            if knight_tour(next_x, next_y, move_count + 1, board, move_x, move_y, N):
                return True
            # Backtrack if no valid move is found
            board[next_x][next_y] = -1
    
    return False

# Initialize the board and move_x, move_y
def solve_knights_tour(N):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    
    # Possible moves for a knight (8 directions)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # Starting position of the knight
    board[0][0] = 0
    
    if knight_tour(0, 0, 1, board, move_x, move_y, N):
        return board
    else:
        return None

# Example usage for a 5x5 board
N = 5
solution = solve_knights_tour(N)

if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists")
