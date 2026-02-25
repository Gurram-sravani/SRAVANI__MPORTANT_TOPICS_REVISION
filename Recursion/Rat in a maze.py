class Solution:
  def rat_in_a_maze(self,n,grid):
    if grid[0][0]==0
      return 0
    n=len(grid)
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    path=[]
    output=[]
    visited=set()
    self.backtrack(spr=0,spc=0,grid,directions,path,output,n,visited)
    return output
  def backtrack(self,0, 0, grid, directions, path, output, n, visited):
    if spr==n-1 and spc==n-1:
      output.append(path.copy())
      return
    path.append((spr,spc))
    visited.add((spr,spc))
    for (r,c) in directions:
        nr = spr + r
        nc = spc + c
        if nr < 0 or nc < 0 or nr >= n or nc >= n or (nr, nc) in visited or grid[nr][nc] == 0:
          continue   ''' Dont use return becaus eif you use return That exits the entire backtrack call right away, so it won’t try the remaining directions.
In backtracking, if one direction is invalid, you should skip it and continue, not stop everything.This will make you miss valid paths.'''
          
          self.backtrack(nr, nc, grid, directions, path, output, n, visited)
    visited.remove((spr, spc))
    path.pop()
        
