Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:
            return False
        if q is None and p is not None:
            return False
        if p is None and q is None:
            return True

        if p.val!=q.val:
            return False
            
        else:
            left= self.isSameTree(p.left,q.left)
            right=self.isSameTree(p.right,q.right)
        return (left and right)
#So I am so confused with recursion returns and function returns. Be careful and think when you are returning. Always try to store the recursion result into a variable if needed and return it . Otherwise, call the recursion function in the return statement which directly returns the value. So here as it is same tree when you are traversing left first make sure that at any point left is False before going to right becaus eif the left subtrees is FALSE then no need to check right , You can exist the function.
