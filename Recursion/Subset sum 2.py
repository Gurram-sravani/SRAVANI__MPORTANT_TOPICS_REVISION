In this problem, Duplicates needs to get avoided as the input array consists of duplicates. 
Normal Approach: You will generate all the substes and use set to avaoid duplicates.
But if you do "sorting" you avoid generating duplicate subsets at all. 

class Solution:
    def subset_sum_2(self,input):
        n=len(input)
        input.sort()
        start=0
        path=[]
        output=[]
        self.backtrack(n,input,start,path,output)
        return output
    def backtrack(self,n,input,start,path,output):
        if start>=n:
            output.append(path.copy())
            return
        for i in range(start,n):
            path.append(input[i])
            if i > start and input[i] == input[i-1]:  # skip duplicates at same depth
                continue
            self.backtrack(n,input,i+1,path,output)
            path.pop()
