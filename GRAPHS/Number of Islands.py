class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len=len(grid)
        col_len=len(grid[0])
        self.no_of_Islands=0
        visited=set()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]=="1" and (r,c) not in visited:
                    self.no_of_Islands+=1
                    self.dfs(grid,r,c,visited,row_len,col_len)
        return self.no_of_Islands

    def dfs(self,grid,r,c,visited,row_len,col_len):
        if 0>r>=row_len or 0>c>=col_len or (r,c) in visited or grid[r][c]=="0":
            return
        visited.add((r,c))
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        for i,j in dir:
            nr=r+i
            nc=c+j
            if 0 <= nr < row_len and 0 <= nc < col_len and (nr,nc) not in visited and grid[nr][nc] == "1":
                self.dfs(grid,nr,nc,visited,row_len,col_len)
            
# so here when you are using visited=set() and checking(r,c) in that visited set taking lot of time. 
'''When I check (r,c) in visited, Python needs to:
create a tuple (r,c)
look it up in a set
set lookup is O(1), but tuple creation + hashing takes time
So marking visited in-place avoids this overhead.'''

'''
dir = [(1,0),(0,1),(-1,0),(0,-1)]
DFS is called once per land cell (in worst case), so this list gets created thousands of times.
Even though the list is small, creating it repeatedly adds overhead.
Better idea:
Define the directions once, not inside DFS, so Python doesn’t allocate that list over and over.
This does not change big-O, but it reduces constant overhead.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len=len(grid)
        col_len=len(grid[0])
        dir=[(1,0),(0,1),(-1,0),(0,-1)] # optimization 2, dont create in dfs because whenever you call dfs dir list will be created if you call for 4 nodes, 4 new lists are created
        no_of_Islands=0
       # visited=set()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]=="1":
                    no_of_Islands+=1
                    self.dfs(grid,r,c,row_len,col_len,dir)
        return no_of_Islands

    def dfs(self,grid,r,c,row_len,col_len,dir):
        if 0>r>=row_len or 0>c>=col_len or grid[r][c]=="0":
            return
        #visited.add((r,c))
        grid[r][c]='0'  # Optimization 1 to avoid checking in visited by creating a tuple(r,c)
        
        for i,j in dir:
            nr=r+i
            nc=c+j
            if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == "1":
                self.dfs(grid,nr,nc,row_len,col_len,dir)
                


Aobe tow are recursive stack approaches .

Below code is Ierative approch :

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1

                    # start DFS using stack
                    stack = [(r, c)]
                    grid[r][c] = "0"   # mark visited immediately

                    while stack:
                        cr, cc = stack.pop()

                        for dr, dc in directions:
                            nr, nc = cr + dr, cc + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"   # mark when pushing
                                stack.append((nr, nc))

        return islands
'''Recursive DFS = implicit stack (slow in Python)
Iterative DFS = explicit stack (faster & safer) '''
