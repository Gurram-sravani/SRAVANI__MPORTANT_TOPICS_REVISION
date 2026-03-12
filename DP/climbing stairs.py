class Solution:
    def climbStairs(self, n: int) -> int:
        memo={i:-1 for i in range(n+1)}
        cnt=self.memo(memo,n)
        return cnt
    def memo(self,memo,i):
        if i in memo and memo[i]!=-1:
            return memo[i]
        if i<=1:
            return 1
        memo[i]=self.memo(memo,(i-1))+self.memo(memo,(i-2))
        return memo[i]
# Time Complexity: O(n)
# Space Complexity: O(n) stack Space + O(n) memo space 

Optimized Version: 
def climbStairs(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return b
# Time Complexity: O(n)
# Space Complexity: O(1)
