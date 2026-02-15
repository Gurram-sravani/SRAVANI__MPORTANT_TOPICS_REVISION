class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        for i in range(len(nums)):
            for k in range(1,n):
                indx=(i+k)%n
                if (nums[indx]>nums[i]):
                    res[i]=nums[indx]
                    break
        return res

# Time complexity:O(n^2)
# Space Complexity: O(n)

#Do not modify the original nums array while computing the next greater elements.
If you replace nums[i] with another value (or -1) during iteration, then future comparisons will use the modified value instead of the original one.

  ''' 
  for k in range(1, n):
      if nums[indx] > nums[i]:
          res[i] = nums[indx]
          break
      else:
          res[i] = -1
  
  You check the first person.
  If they are NOT taller, you immediately say:
  Okay, nobody is taller than me. You haven't checked the rest yet.
  So this else runs too early — after just one failed comparison.
  That’s the core problem 

****************************************************************************

def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        for i in range(len(nums)):
            for k in range(1,n):
                indx=(i+k)%n
                if (nums[indx]>nums[i]):
                    res[i]=nums[indx]
                    break
            else:
                res[i]=-1
        return res

  
This else means (for-else LOOP):
"If I finished the entire search and never found what I was looking for, then do this."
**********************************************************************************************

Optimised version:

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        nge=[0]*n
        
        for i in range((2*n)-1,-1,-1):  # expanding the array with same (doubling the array )
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            if not stack:
                nge[i%n]=-1
            else:
                nge[i%n]=stack[-1]
            stack.append(nums[i%n])
        return nge
# Time complexity: O(2n) =>O(n)
# Space Complexity: O(n) stack + output list O(n) 
