# You need to check only one recursion at atime , be careful when returning -
either take a variable to store the traversal result or try to return travsersal result in return statement.
And also try checking or taking the left and right value sinto root.left and root.right because you need to add the nes val to root.left or root.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        root=self.traversal(root,val)
        return root
    
    def traversal(self,root,val):
        if root is None:
            root=TreeNode(val)
            return root 
        if root.val>val:
            root.left=self.traversal(root.left,val)
        else:
            root.right=self.traversal(root.right,val)
        return root

# time Complexity :O(n)
# Space Compelxity : O(n) recursion stack
