''' Height - How tall is the tree below me, Height increases as you go upward
Depth (distance from root down to a node),Increases as you go down '''

'''The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them. '''

'''We return max(leftHeight, rightHeight) because height represents the longest single downward path that can be extended upward,
while diameter considers both sides only locally, we need to take max(leftheight, rightheight) as we have need to consider longest path from both sides'''\

#Diameter=Leftheight+rightHeight

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        self.longest=max(self.longest,left+right)
        return 1+max(left,right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest=0
        self.height(root)
        return self.longest


''' Looking at pointers only tells you:

“Does this node have a left child?”

“Does this node have a right child?”

But height is NOT:

“How many children do I have?”

Height is:

“How far down does the tree go from me?” '''
