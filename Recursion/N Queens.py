class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output=[]
        path=[]
        rows=0
        empty_board=[["."]*n for i in range(n)]
        self.backtrack(rows,output,empty_board,n,cols=set(),diagonals=set(),anti_diagonals=set())
        return output
    def create_board(self,state):
        board = []
        for row in state:
            board.append("".join(row))
        return board       

    def backtrack(self, rows, output, state, n, cols, diagonals, anti_diagonals):
        if rows==n:
            output.append(self.create_board(state))
            return
        for col in range(n):
            curr_diagonal=rows-col  # Same Diagonals
            curr_anti_diagonal=rows+col  # Opposite Diagonals
            if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                continue
            cols.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)
            state[rows][col]="Q"
            self.backtrack(rows+1,output,state,n,cols,diagonals,anti_diagonals)
            cols.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)
            state[rows][col]="."

# Time Complexity: N!
# Space Compelxity : O(N^2)
