class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1 for i in range(len(nums))]
        i=0
        self.memo_func(nums,memo,i)
        return self.memo_func(nums, memo, i)
    def memo_func(self,nums,memo,i):
        if i>=len(nums):
            return 0
        if memo[i]!=-1:
            return memo[i]
        
        skip=self.memo_func(nums,memo,i+1)
        take=nums[i]+self.memo_func(nums, memo, i+2)
        memo[i]=max(skip,take) 
        return memo[i]
