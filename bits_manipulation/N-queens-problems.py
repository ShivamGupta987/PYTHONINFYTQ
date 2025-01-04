def solveNQueens(n):
    # row -> jis row me hame new queen place krna hai
    # queens -> already placed position  
    def backtrack(row, cols, left_diagonal, right_diagonal, queens):
        # Agar sabhi queens place ho chuki hain
        if row == n:
            # yahan hum solution ko append karenge
            result.append(queens[:])
            return
        
        # Har column ke liye check karna hai
        for col in range(n):
            # Check karo agar queen ko place karna safe hai
            if not (cols & (1 << col)) and not (left_diagonal & (1 << (row + col))) and not (right_diagonal & (1 << (row - col + n - 1))):
                # Update karo mask to mark this column and diagonals as occupied
                cols ^= (1 << col)
                left_diagonal ^= (1 << (row + col))
                right_diagonal ^= (1 << (row - col + n - 1))
                
                # Queen place kar do aur backtrack karo agle row par
                queens.append(col)
                backtrack(row + 1, cols, left_diagonal, right_diagonal, queens)
                
                # Backtrack - undo previous decision
                queens.pop()
                cols ^= (1 << col)
                left_diagonal ^= (1 << (row + col))
                right_diagonal ^= (1 << (row - col + n - 1))
    
    result = []
    backtrack(0, 0, 0, 0, [])
    return result

# Use the function for N = 4
solutions = solveNQueens(4)
print(solutions)
