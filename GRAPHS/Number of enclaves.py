class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row_len=len(grid)
        col_len=len(grid[0])
        count=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        for r in range(row_len):
            for c in range(col_len):
                if (r == 0 or r == row_len - 1 or  c == 0 or c == col_len - 1):
                    if grid[r][c]==1:
                        self.dfs(grid,row_len,col_len,count,directions,r,c)
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]==1:
                    count+=1
        return count
                
                    
        return count
    def dfs(self,grid,row_len,col_len,count,directions,r,c):
        if r<0 or r>=row_len or c<0 or c>=col_len  or grid[r][c]==0:
            return 
        grid[r][c]=-1
        for i,j in directions:
            nr=r+i
            nc=c+j
            if nr<0 or nr>=row_len or nc<0 or nc>=col_len or grid[nr][nc]==0:
                continue   # if you use return here , That return exits the entire DFS immediately.So if even one neighbor is invalid (which happens constantly),DFS stops exploring all other directions.That is why many boundary-connected lands are not erased 
            if grid[nr][nc]==1:
                grid[nr][nc]==-1
                self.dfs(grid,row_len,col_len,count,directions,nr,nc)
        return count

# Time Complexity:O(m*n) to call dfs if boundari is 1 + O(m*n) to check remaining 1s and to count => O(m*n)
# Space Complexity: O(m*n) recursion stack space 
