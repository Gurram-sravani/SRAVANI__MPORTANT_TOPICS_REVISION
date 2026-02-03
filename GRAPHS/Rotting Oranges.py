
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.queue=deque()
        self.no_of_minutes=0
        self.fresh_oranges=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        row_len=len(grid)
        col_len=len(grid[0])
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]==2:
                    self.queue.append((r,c))
                elif grid[r][c]==1:
                    self.fresh_oranges+=1
        if self.fresh_oranges==0:
            return 0
            
        while self.queue and self.fresh_oranges:
            for i in range(len(self.queue)):
                r,c=self.queue.popleft()
                for i,j in directions:
                    nr=r+i
                    nc=c+j
                    if (nr>=0) and (nc>=0) and (nr<len(grid)) and (nc<len(grid[0])): 
                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            self.queue.append((nr,nc))
                            self.fresh_oranges-=1
            self.no_of_minutes+=1
            print(self.no_of_minutes)
        
        if self.fresh_oranges!=0:
            return -1
        else:
            return self.no_of_minutes

# time Complexity : Adding elements into Queue :O(m.n) + bfs while loop Worst case O(m.n) => O(mn)
# Space Complexity : Queue : O(m.n) 
