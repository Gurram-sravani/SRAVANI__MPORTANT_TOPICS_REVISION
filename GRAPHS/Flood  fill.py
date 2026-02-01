class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_len=len(image)
        col_len=len(image[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        src_color=image[sr][sc]
        self.dfs(image,sr,sc,directions,color,src_color,row_len,col_len)
        return image
        
    def dfs(self, image,sr,sc,directions,color, src_color,row_len,col_len):
        if 0>sr>=row_len or 0>sc>=col_len or image[sr][sc]!=src_color or src_color==color:
            return
        image[sr][sc]=color
        for r,c in directions:
            nr=sr+r
            nc=sc+c
            if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len :
                continue
            elif  image[nr][nc]==src_color:
                self.dfs(image,nr,nc,directions,color,src_color,row_len,col_len)

# Time complexity : O(1) directions * O(m*n) if all the adjacent cells gets conencted from starting point in worst case as it traverse all the cells 
# Space Complexity: O(m × n) in the worst case for recursion stack

One Optimization for above is checking the starting point is same as color before callign the dfs

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_len=len(image)
        col_len=len(image[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        src_color=image[sr][sc]
        if src_color==color:
          return 
        else:
          self.dfs(image,sr,sc,directions,color,src_color,row_len,col_len)
        return image
        
    def dfs(self, image,sr,sc,directions,color, src_color,row_len,col_len):
        if 0>sr>=row_len or 0>sc>=col_len or image[sr][sc]!=src_color or src_color==color:
            return
        image[sr][sc]=color
        for r,c in directions:
            nr=sr+r
            nc=sc+c
            if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len :
                continue
            elif  image[nr][nc]==src_color:
                self.dfs(image,nr,nc,directions,color,src_color,row_len,col_len)

# Time complexity : O(1) directions * O(m*n) if all the adjacent cells gets conencted from starting point in worst case as it traverse all the cells 
# Space Complexity: O(m × n) in the worst case for recursion stack
