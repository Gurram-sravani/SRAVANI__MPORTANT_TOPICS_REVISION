class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s) 
        word_Set=set(wordDict)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(0,n+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in word_Set:
                    dp[i]=True
                    break 
        return dp[n]
Time Complexity:O(N^3) 
Space Complexity:O(n) +O(m) set 
# The time complexity is O(n²) in standard analysis, though substring creation can make it O(n³) in strict terms.

