In below approach : You will get TIME LIMIT EXCEEDED ERROR
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
OPTIMIZED APPROACH: 

from typing import List

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        # --- ADDED: O(1) constraint tables ---
        self.rows = [[False] * 10 for _ in range(9)]
        self.cols = [[False] * 10 for _ in range(9)]
        self.boxes = [[False] * 10 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    d = int(board[r][c])
                    b = (r // 3) * 3 + (c // 3)
                    self.rows[r][d] = True
                    self.cols[c][d] = True
                    self.boxes[b][d] = True

        self.backtrack(board)
    def backtrack(self, board: List[List[str]]) -> bool:
        n = 9

        # --- MRV: find the empty cell with minimum candidates ---
        best_r = best_c = -1
        best_box = -1
        min_options = 10

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    b = (r // 3) * 3 + (c // 3)

                    options = 0
                    for digit in range(1, 10):
                        if (not self.rows[r][digit] and
                            not self.cols[c][digit] and
                            not self.boxes[b][digit]):
                            options += 1

                    if options == 0:
                        return False

                    if options < min_options:
                        min_options = options
                        best_r, best_c, best_box = r, c, b
                        if min_options == 1:
                            break
            if min_options == 1:
                break

        # no empty cell left
        if best_r == -1:
            return True

        r, c, b = best_r, best_c, best_box

        for digit in range(1, 10):
            if (not self.rows[r][digit] and
                not self.cols[c][digit] and
                not self.boxes[b][digit]):

                ch = str(digit)
                board[r][c] = ch

                self.rows[r][digit] = True
                self.cols[c][digit] = True
                self.boxes[b][digit] = True

                if self.backtrack(board):
                    return True

                self.rows[r][digit] = False
                self.cols[c][digit] = False
                self.boxes[b][digit] = False
                board[r][c] = "."

        return False

    def isValid(self, board: List[List[str]], r: int, c: int, ch: str) -> bool:
        digit = int(ch)
        b = (r // 3) * 3 + (c // 3)

        # --- CHANGED: O(1) checks instead of scanning loops ---
        if self.rows[r][digit]:
            return False
        if self.cols[c][digit]:
            return False
        if self.boxes[b][digit]:
            return False

        return True
