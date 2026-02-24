class Solution:
  def rat_in_a_maze(self,n,grid):
    n=len(grid)
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    path=[]
    output=[]
    self.backtrack(spr=0,spc=0,grid,directions,path,output,n)
  def self.backtrack(spr,spc,grid,directions,path,output,n)
    if spr=n-1 and spc=n-1:
      output.append(path.copy())
      return
    path.append((r,c))
    for r in range(len(grid)):
      for c in range(len(grid[0]):
        if r<0 or c<0 or r>=len(grid) or c>=len(len(grid[0]):
          return
        if grid[r][c]==0:
          continue
          spr=spr+r
          spc=spc+c
          self.backtrack(spr,spc,grid,directions,path,output,n)
          path.pop()
        
