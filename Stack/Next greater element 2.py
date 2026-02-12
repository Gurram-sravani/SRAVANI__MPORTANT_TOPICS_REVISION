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
  That’s the core problem '''

*************************************************************************************

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
