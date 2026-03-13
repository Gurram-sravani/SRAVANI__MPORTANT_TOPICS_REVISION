class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[-1]*n for i in range(m)]
        return self.paths(m, n, memo,r=0,c=0)

    def paths(self,m,n,memo,r,c):
        if r>=m or c>=n:
            return 0
        if r==m-1 and c==n-1:
            return 1
        if memo[r][c]!=-1:
            return memo[r][c]
        total=self.paths(m, n, memo, r, c+1)+self.paths(m, n, memo, r+1, c)
        if r<m and c<n:
            memo[r][c]=total
        return total

TIME COMPLEXITY: O(mn) 
SPACE COMPLEXITY : O(mn) MEmo +O(m+n) Recursion stack => O(mn) 
