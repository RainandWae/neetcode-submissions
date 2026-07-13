class Solution:
    #BFFFFFF
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 row total, start 0 end 8(9 total)
        for row in range(9):
            # set() use for dupe, (1,2,3,3,1) --> (1,2,3)
            seen = set()
            # each row have 9 cell
            for i in range(9):
                #skip "." == empty
                if board[row][i] == ".":
                    continue
                
                # catching dupe
                if board[row][i] in seen:
                    return False
                # no dupe, add into seen
                seen.add(board[row][i])

        # repeat in column
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        # 9 square in total
        for square in range(9):
            seen = set()
            # i, j range 3, coordinate of cell, 0.0, 0.1, ..., 2.2
            for i in range(3):
                for j in range(3):
                    # square and cell calcuation, coordinate start at top left. 
                    # since hard to isolate actual square just start from
                    # 1 to 9(0 to 8) 
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    # row square // ==> going to move like 000111222
                    # column square % ==> going to move like 012012012
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True