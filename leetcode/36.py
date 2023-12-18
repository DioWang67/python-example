

def isValidSudoku(board):
    rows = [set() for _ in range(9)]  # 每行的數字集合
    cols = [set() for _ in range(9)]  # 每列的數字集合
    boxes = [set() for _ in range(9)]  # 每個 3x3 子盤面的數字集合
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != ".":
                if num in rows[i] or num in cols[j] or num in boxes[(i // 3) * 3 + j // 3]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)
    # print(rows)
    return True


# 測試
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","."]
]

print(isValidSudoku(board))  # 預期輸出：True

# board = [
#     ["5","3",".",".","7",".",".",".","."]]

# for i in range(9):
#     for j in range(9):
#         num = board[i][1]
#         print(num)
