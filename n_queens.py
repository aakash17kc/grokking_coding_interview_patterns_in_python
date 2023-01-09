def is_valid_move(row, col, sol):
    for i in range(0, row):
        old_row = i
        old_col = sol[i]
        diagonal_offset = row - old_row
        if old_col == col or old_col == col - diagonal_offset or old_col == col + diagonal_offset:
            return False
    return True


def solve_n_queens(n):
    sol_stack = []
    sol = [-1] * n
    row = 0
    col = 0
    res = []

    while row < n:
        while col < n:
            if is_valid_move(row, col, sol):
                # If this is a safe position for a queen (a valid move), save
                # it to the current solution on the stack...
                sol_stack.append(col)
                sol[row] = col
                row = row + 1
                col = 0
                # ... and move on to checking the next row (breaking out of the inner loop)
                break
            col = col + 1
        if col == n:
            if sol_stack:
                row = row - 1
                col = sol_stack[-1] + 1
                sol_stack.pop()
            else:
                break
        if row == n:
            res.append(sol)
            row = row - 1
            col = sol_stack[-1] + 1
            sol_stack.pop()
    return res

if __name__ == '__main__':
     print(n_queens(4))