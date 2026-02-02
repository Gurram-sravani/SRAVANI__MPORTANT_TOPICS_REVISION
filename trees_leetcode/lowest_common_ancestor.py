# BRUTE FORCE APPROACH:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_seen=[]
        q_seen=[]
        common_char=None
        self.common(root,p,p_seen)
        self.common(root,q,q_seen)
        i=0
        if len(p_seen)<len(q_seen):
            while i<len(p_seen):
                if p_seen[i]==q_seen[i]:
                    common_char=p_seen[i]
                i+=1
        else:
            while i<len(q_seen):
                if p_seen[i]==q_seen[i]:
                    common_char=q_seen[i]
                i+=1
        return common_char

    def common(self,root,target,path):
        if root is None:
            return
        path.append(root)
        if root==target:
            return True
        left=self.common(root.left,target,path)
        if left is True:
            return True
        right=self.common(root.right,target,path)
        if right is True:
            return True
        path.pop()  # If I dont find the target in left and right the node needs to get deleted (backtrack starts here)
        return False

# Time Complexity: O(n) to find p_seen list +O(n) to find q_seen + O(n) to find common char (traversing list)
#Space Complexity: O(h) (p_seen)+O(h) q_seen + O(h) recursion stack 
''' Your p_seen and q_seen lists store a path, not the whole subtree: 
When you find p, you are storing: root → ... → p
That is one single chain of nodes.
How long can that chain be?
At most the number of levels from root to that node = height h '''

# Optimised Approavh : Return Node approach 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def common_node(self,root,p,q):
        if root is None:
            return None
        if root==p or root==q:
            return root 
        left=self.common_node(root.left,p,q)
        right=self.common_node(root.right,p,q)
        if left and right:
            return root
        return left or right
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.common_node(root,p,q)
# Time complexity :O(n)
# sPace complexity :O(h) Recursion stack Space

