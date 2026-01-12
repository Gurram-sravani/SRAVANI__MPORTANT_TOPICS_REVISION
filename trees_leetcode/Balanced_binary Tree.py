''' A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.'''
'''What does “balanced” mean : Each level splits nodes into two halves , Tree grows wide, not tall
"You need to calculate the height of each sub tree from LEFT & RIGHT and check the difference abs(left-right)>1 , 
Then it is not balanced .So in trees, there are subtrees so if any subtree is unbalanced then you can return ,
no need of checking it further. So to track this update, take a instance variable with TRUE. Whenever you hit the difference greater than 1 ,
then make it as FALSE and return.
So when returning here if you just write ""return"" - you will get an ERROR saying that ""TypeError: ... NoneType - NoneType""  
if abs(left-right) > 1:
  self.isBalanced = False
  return          # <- this returns None implicitly (Throws an error) => return self.isBalanced" '''

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
        print(left)
        right=self.height(root.right)
        print(right)
        if abs(left-right)>1:
            self.isBalanced=False
            return self.isBalanced 
        return 1+max(left,right)

    def isBalanced(self,root):
        self.isBalanced=True
        self.height(root)
        return self.isBalanced
        
