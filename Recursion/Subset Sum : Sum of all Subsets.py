#Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.
class Subset:
  def subset_sum(self,input):
    output=[]
    path=[]
    n=len(input)
    index=0
    self.backtrack(input,output,path,n,index)
    output.sort()
    return output  
sort() returns None
  def backtrack(self,input,output,path,n,index):
    if index>=n:
        output.append(sum(path.copy()))
        return
    path.append(input[index])
    self.backtrack(input,output,path,n,index+1)
    path.pop()
    self.backtrack(input,output,path,n,index+1)

Sol=Subset()
a=[5,1,2]
result=Sol.subset_sum(a)
print(result)

b=[3,1,2]
b_result=Sol.subset_sum(b)
print(b_result)

# Time Complexity: 2^n Subsets for every n and doing sum => O(n.2^n)  + Sorting O(2^nlog2^n) -> Since log s^n is "n" -> O(2^n⋅n)
because sort uses Tim sort and you are sorting all subsets => Final Time  O(n.2^n)+O(n.2^n)=> O(n.2^n)

# Space Complexity: Stack Space O(n)  auxilary space+ path O(n) + output O(2^n) => O(2^n)

''' 
Dont write directly return output.sort() It will return None because sort operation worka in-place. 
So Python does this in two steps:
output.sort() → sorts the list in place, sort() returns None => return None '''

# if path is [] => empty list which is not None => sum([]) returns 0 

OPTIMIZED APPROACH:

''' At every leaf (each subset), you do:
output.append(sum(path))
sum(path) takes O(length of path), up to O(n).
You do that for 2^n subsets → O(n · 2^n) just for summing''' 

class Subset:
    def subset_sums(self, arr):
        output = []
        self.dfs(arr, 0, 0, output)   # index=0, curr_sum=0
        return sorted(output)         # or output.sort(); return output

    def dfs(self, arr, index, curr_sum, output):
        if index == len(arr):
            output.append(curr_sum)
            return

        # include arr[index]
        self.dfs(arr, index + 1, curr_sum + arr[index], output)

        # exclude arr[index]
        self.dfs(arr, index + 1, curr_sum, output)


Sol = Subset()
print(Sol.subset_sums([5, 1, 2]))

**** IMP: Here curr_sum is an integer.Integers are immutable.Each recursive call gets its own copy.

Time:
DFS visits each subset once → O(2^n)
Sorting 2^n Sums=> O(2^nlog2^n) -> Since log s^n is "n" -> O(2^n⋅n)
Final Time : O(n · 2^n) (sorting dominates)
But you did remove wasted work: generation becomes O(2^n) instead of O(n·2^n).

Space: 

Output: O(2^n)
Recursion stack: O(n)
No path list anymore
