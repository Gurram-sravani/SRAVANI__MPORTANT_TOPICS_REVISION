It’s not O(n).
At each index you do 2 choices (take / not take), so total calls/leaves are about 2ⁿ.
Also, at every leaf you do output.copy() which costs O(k) (k up to n). Across all subsets, total copying cost is O(n·2ⁿ).
Time = O(n · 2ⁿ)  => generating 2ⁿ subsets, each up to length n.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[]
        self.path=[]
        n=len(nums)
        index=0
        return self.dfs(index,n,output,nums)
    def dfs(self,index,n,output,nums):
        if index>=n:
            self.path.append(output.copy())
            return 
        output.append(nums[index])
        self.dfs(index+1,n,output,nums)
        output.pop() # dont us eremove function because If nums had duplicates like [1,2,2], remove(2) removes the first 2, not necessarily the one you just added. pop() always removes the last added, which matches backtracking.
        self.dfs(index+1,n,output,nums)
        return self.path

# Time Complexity: O(n · 2ⁿ)
# Space Complexity : O(n · 2ⁿ)
