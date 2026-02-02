import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum=(-math.inf)
        self.path_sum(root)
        return self.max_path_sum

    def path_sum(self,root):
        if root is None:
            return 0
        path.append(root)
        left=self.path_sum(root.left)
        right=self.path_sum(root.right)
        
        left = max(0, left)     
        right = max(0, right)    

        self.max_path_sum=max(self.max_path_sum,root.val+left+right)
        return root.val+max(0,left,right)

# Time Complexity: O(n) 
# Space Complexity: O(h) Recursion Stack 

''' when you only have root [-3] , In this case you need to think of taking
self.max_path_sum=(-math.inf) because if it is 0 when you return max value it will get 0 as output which is wrong. 
Think of recursion like this:

“Go all the way down first, then build answers on the way back up.”

Downward return = “What’s the best I can give my parent?”

Global update = “What’s the best path that passes through me ''
