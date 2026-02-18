class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]
        path=[]
        index=0
        self.backtrack(output,path,candidates,target,index)
        return output
    
    def backtrack(self,output,path,candidates,target,index):
        if sum(path)==target: 
            output.append(path.copy())
            return
        if index>=len(candidates) or sum(path)>target:
            return 
        path.append(candidates[index])
        self.backtrack(output, path, candidates, target, index)
        path.pop()
        self.backtrack(output, path, candidates, target, index+1)

# Dont check index>len(list_size) becaus eif you check this even the path sum is target , without adding to the output it will return back 
# time complexity :

