Substring is a contigous , cannot skip any index, must be defind as [start:end+1]  => Substring logic = choose start and end
subsequence  Does NOT need to be contiguous, can skip index, keep original order => Subsequence logic = take / skip pattern

# Partitioning by every index for every string (so you need to do the partition for a string from start to end of the string).

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        result=[]
        index=0
        self.backtrack(s, result, path, index)
        return result
    def palindrome(self,s):
        if s==s[::-1]:
            return True
        return False
    def backtrack(self,s,result,path,index):
        if index==len(s):
            result.append(path.copy())
            return 
        for i in range(index,len(s)):
            if self.palindrome(s[index:i+1]):
                path.append(s[index:i+1])
                self.backtrack(s,result,path, i+1)
                path.pop()

So you will do partition by every index , for each index (0...n, 1..n, 2..n .......n) 
