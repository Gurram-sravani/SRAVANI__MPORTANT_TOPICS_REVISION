

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        self.queue=deque()
        self.queue.append(root)
        result=[]
        while self.queue:
            current_level=[]
            size=len(self.queue)
            for i in range(size):
                node=self.queue.popleft()
                current_level.append(node.val)
                print(current_level)
                if node.left is not None:
                    self.queue.append(node.left)
                    #print(self.queue)
                if node.right is not None:
                    self.queue.append(node.right)
            result.append(current_level)
        return result
#Time complexity:O(h) if given tree is balanced then it is O(log n) (h==log n) or if it is skewed O(n) (h==n)
# Space Complexity: O(h) 


