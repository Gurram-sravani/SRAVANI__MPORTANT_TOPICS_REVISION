''' so here you have few bases cases to check and go to traversal.
As it is BST , at first you need to check key is greater or less than root.
if it root>key  then you need to check root.left is not none and root.left ==key until you find keep traversing left only as key is less than root.
if it greater than right , you need to check root.right is not none and root.right ==key until you find keep traversing right only as key is greater than root.
Make sure you store original root in another variable before traversal because if you dont find the key you just need to return root 
but if you dont store the original root in another variable after checkign left or right , if you return root => It will return None.
If you find the key then I am appending the right part to the left of the key in the tree so thats why you need to check last nod ein left and need to append the right part of key. '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            return self.traversal(root,key)
        
        original = root
        cur = root
        while cur is not None:
            if cur.val>key:
                if cur.left is not None and cur.left.val==key:
                    cur.left=self.traversal(cur.left,key)
                    break
                else:
                    cur=cur.left       
            else:
                if cur.right is not  None and cur.right.val==key:
                    cur.right=self.traversal(cur.right,key)
                    break
                else:
                    cur=cur.right
        return original
        
    def traversal (self,root,key):
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        right_child=root.right
        last_node=self.last_node(root.left)
        last_node.right=right_child
        return root.left
    def last_node(self,root):
        if root.right is None:
            return root
        
        return self.last_node(root.right)

# Time Complexity: O(h)
# Space Complexity :O(h) Recursion Stack -> Height of the tree 
