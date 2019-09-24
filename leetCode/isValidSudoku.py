from typing import List

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次
# [ ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]]


def checkList(arr: List[str]) -> bool:
    res = []
    for i in arr:
        if not i.__eq__("."):
            res.append(i)
    return len(res) == len(set(res))


def isValidSudoku(board: List[List[str]]) -> bool:
    #  check Row
    for strs in board:
        if not checkList(strs):
            return False

    #  check Column
    for i in range(9):
        arr = []
        for j in range(9):
            arr.append(board[j][i])
        if not checkList(arr):
            return False

    #  check 3x3
    for n in range(3, 12, 3):
        for m in range(3, 12, 3):
            arr = []
            for i in range(n-3, n):
                for j in range(m-3, m):
                    arr.append(board[i][j])
            if not checkList(arr):
                return False

    return True


arr = [[".",".",".",".","5",".",".","1","."],
       [".","4",".","3",".",".",".",".","."],
       [".",".",".",".",".","3",".",".","1"],
       ["8",".",".",".",".",".",".","2","."],
       [".",".","2",".","7",".",".",".","."],
       [".","1","5",".",".",".",".",".","."],
       [".",".",".",".",".","2",".",".","."],
       [".","2",".","9",".",".",".",".","."],
       [".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(arr))
