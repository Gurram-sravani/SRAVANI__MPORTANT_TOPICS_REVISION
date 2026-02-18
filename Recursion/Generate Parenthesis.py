class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        closed_counter=n
        open_counter=n
        new_str=""
        self.path=[]
        self.dfs(closed_counter,open_counter,new_str)
        return self.path
    def dfs(self,closed_counter,open_counter,new_str):
        if closed_counter==0 and open_counter==0:
            self.path.append(new_str)
            return
        if open_counter>0:
                self.dfs(closed_counter,open_counter-1,new_str+"(")
        if closed_counter>0 and open_counter<closed_counter:
                new_str+")"
                self.dfs(closed_counter-1,open_counter,new_str+")")


# becareful when you are passing strings , check how string append works here when backtracking understand this concept more 


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.dfs(open_left=n, close_left=n, new_str="")
        return self.ans

    def dfs(self, open_left: int, close_left: int, new_str: str) -> None:
        # base case: used all parentheses
        if open_left == 0 and close_left == 0:
            self.ans.append(new_str)
            return

        # Option 1: add "(" if we still have opens left
        if open_left > 0:
            new_valid_str = new_str + "("
            self.dfs(open_left - 1, close_left, new_valid_str)

        # Option 2: add ")" only if it won't break validity
        # Valid rule: we can close only if we have more closes left than opens left
        # (meaning we have an unmatched "(" already placed)
        if close_left > open_left:
            new_valid_str = new_str + ")"
            self.dfs(open_left, close_left - 1, new_valid_str)
