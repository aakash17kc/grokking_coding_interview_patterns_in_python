from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    r = len(board)
    c = len(board[0])
    found = False

    def dfs(row, col, wrd):
        if len(wrd) == 0:
            return True
        if row < 0 or col < 0 or row == r or col == c or board[row][col] != wrd[0]:
            return False
        board[row][col] = '#'
        res = False
        for d in dir:

            res = dfs(row + d[0], col + d[1], wrd[1:])
            if res:
                break
        board[row][col] = wrd[0]
        return res



    for i in range(r):
        for j in range(c):
            if dfs(i, j, word):
                return True

    return False


if __name__ == '__main__':
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
