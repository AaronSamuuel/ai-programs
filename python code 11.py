def solve_queens(n):
    board = [-1] * n  # board[row] = column of queen
    result = []

    def is_valid(row, col):
        for i in range(row):
            # Check column & diagonals
            if board[i] == col or abs(row - i) == abs(col - board[i]):
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append(list(board))
            return
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # reset

    backtrack(0)
    return result


# Solve 8-Queens
solutions = solve_queens(8)

# Print all solutions
for solution in solutions:
    for row in range(8):
        line = ""
        for col in range(8):
            if solution[row] == col:
                line += "Q "
            else:
                line += "- "
        print(line)
    print("\n")
