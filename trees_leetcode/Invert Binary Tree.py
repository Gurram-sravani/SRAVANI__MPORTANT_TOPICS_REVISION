''' When you are working with this Problem make sure you are changing the root.left and root.right value
because if you do like left,right=right,left then the root values will not get change because you are just swapping 2 variable result not changing in the given Tree.
You need to Swap for the given Root . Only assignments to root.left and root.right change the tree'''

''' BOTTOM UP APPROACH: swaps LAST (after children are done) -> POSTORDER: 
Order:
➡ left subtree
➡ right subtree
➡ swap current node
-> It goes all the way to the leaf. Then swaps on the way back up
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left=self.invertTree(root.left)
        right=self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root

''' TOP DOWN APPROACH: PREORDER -> Before recursion
Order:
➡ swap current node
➡ left subtree
➡ right subtree
