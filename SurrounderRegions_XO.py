from _ast import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        borders = []
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 'E'
            if row < rows - 1:
                dfs(row + 1, col)
            if col < cols - 1:
                dfs(row, col + 1)
            if row > 0:
                dfs(row - 1, col)
            if col > 0:
                dfs(row, col - 1)

        for i in range(rows):
            borders.append([i, 0])
            borders.append([i, cols - 1])
        for j in range(cols):
            borders.append([0, j])
            borders.append([rows - 1, j])
        for cell in borders:
            dfs(cell[0], cell[1])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'