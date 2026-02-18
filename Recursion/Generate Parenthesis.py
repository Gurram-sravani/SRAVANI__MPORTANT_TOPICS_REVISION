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
