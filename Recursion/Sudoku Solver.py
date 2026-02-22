In below approach :
''' Validity check is O(27) every try
For every empty cell you try up to 9 digits, and for each digit you scan:
9 cells in the row
9 cells in the column
9 cells in the 3×3 box
That’s ~27 comparisons per digit try.
You recompute the same checks again and again
During recursion, you revisit cells many times. The expensive scanning happens at every node of the search tree. On hard Sudoku boards, the search tree is huge → scanning makes it too slow.
''' 
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.backtrack(board)
    def backtrack(self, board: List[List[str]]) -> bool:
        n = 9
        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":

                    for digit in range(1, 10):
                        ch = str(digit)

                        if self.isValid(board, r, c, ch):
                            board[r][c] = ch

                            if self.backtrack(board):
                                return True

                            board[r][c] = "."   # undo (backtrack)

                    return False   # no digit works here
        return True   # no empty cell left → solved
    def isValid(self, board: List[List[str]], r: int, c: int, ch: str) -> bool:
        # check row
        for j in range(9):
            if board[r][j] == ch:
                return False
        # check column
        for i in range(9):
            if board[i][c] == ch:
                return False
        # check 3x3 box
        br = (r // 3) * 3
        bc = (c // 3) * 3
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if board[i][j] == ch:
                    return False

        return True
# So the fix is: keep your backtracking, but make isValid O(1) by storing “used digits” in fast lookup structures, and update them when you place/remove a digit.
