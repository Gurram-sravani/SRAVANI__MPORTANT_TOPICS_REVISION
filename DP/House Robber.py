class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[n-1]

Memoization:

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
