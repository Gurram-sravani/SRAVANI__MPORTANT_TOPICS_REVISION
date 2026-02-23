class Permutation:
    def permutation_in_array(self, nums):
        n = len(nums)
        output = []
        path = []
        used = set()
        self.backtrack(nums, n, output, path, used)
        return output

    def backtrack(self, nums, n, output, path, used):
        if len(path) == n:
            output.append(path.copy())
            return

        for i in range(n):
            if i in used:
                continue

            # choose
            used.add(i)
            path.append(nums[i])

            # explore
            self.backtrack(nums, n, output, path, used)

            # un-choose
            path.pop()
            used.remove(i)
# Time complexity: n!*n
# Space Complexity:  O(N! * N) + O(N)

Optimized Approach: In this approach, I am not using any "used array" to store the index

class Permutation:
    def permutation_in_array(self,input):
        n=len(input)
        index=0
        output=[]
        self.backtrack(n,output,input,index)
        return output
    def swap(self,input,a,b):
        input[a],input[b]=input[b],input[a]
        return 

    def backtrack(self,n,output,input,index):
        if index>=n:
            output.append(input[:])
            return
        
        for i in range(index,n):
            self.swap(input,index,i)
            self.backtrack(n,output,input,index+1)
            self.swap(input,i,index)

Time complexity:  O(N! * N) 
Space Complexity:  O(N! * N) 
