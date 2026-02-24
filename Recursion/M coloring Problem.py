class Solution:
  def m_coloring(self,m,n,edges,E):
    count=0
    color_Added=set()

    if count>m:
      return 0
    for r,c in edges:
      if r!=c and (r,c) not in color_Added:
        count+=2
        color_Added.add((r,c))
      elif (r,c) in color_Added:
        
      
      
