from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue=deque()
        queue.append(root)
        right_side=[]
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            right_side.append(node.val)
        return right_side

# Time Complexity :O(n) while loop + O(n) current level (for loop) Worst case  => O(n)
# Space Complexity: Queue O(n) + right_side O(h) (h<=n) Worst case => O(n) 
# BFS space depends on width, not height

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        right_side=[]
        self.dfs(root,0,right_side)
        return right_side
    def dfs(self,root,level,right_side):
        if root is None:
            return []
        if level==len(right_side):
            right_side.append(root.val)
        
        self.dfs(root.right,level+1,right_side)
        self.dfs(root.left,level+1,right_side) 

# Time Complexity:O(n)
# Space Complexity: O(h) recursion stack space + O(h) Right_view => O(h)
