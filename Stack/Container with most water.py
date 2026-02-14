#Using two pointer approach :

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_amount=0
        while left<=right:
            width=right-left
            if height[left]<height[right]:
                min_height=height[left]
                left+=1
            else:
                min_height=height[right]
                right-=1
            max_amount=max(max_amount,width*min_height)
        return max_amount
# Time Complexity : O(n)
# Space Complexity:O(1) 
