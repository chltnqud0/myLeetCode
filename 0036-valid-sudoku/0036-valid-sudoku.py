class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            flag = [False] * 9
            for v in board[i]:
                if v != ".":
                    if flag[int(v) - 1]:
                        return False
                    else:
                        flag[int(v) - 1] = True
        

        for i in range(9):
            flag = [False] * 9
            for j in range(9):
                if board[j][i] != ".":
                    if flag[int(board[j][i]) - 1]:
                        return False
                    else:
                        flag[int(board[j][i]) - 1] = True
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                flag = [False] * 9  
                for n in range(3):
                    for k in range(3):
                        if board[j+n][i+k] != ".":
                            if flag[int(board[j+n][i+k]) - 1]:
                                return False
                            else:
                                flag[int(board[j+n][i+k]) - 1] = True
        

        return True