
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):   
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if not stack:
                nge[nums2[i]]=-1
            else:
                nge[nums2[i]]=stack[-1]
            stack.append(nums2[i])
        for ele in range(len(nums1)):
            nums1[ele]=nge[nums1[ele]]
        return nums1

# Time Complexity: O(n) first for loop +O(k) k is length of nums1 => O(n+k)
# Space Complexity: O(n) Stack Space 

# These are the erros you did in this Problem , Be careful next time.

1.stack is not None ≠ “stack is not empty”.
2.Using .isEmpty() / .top as if stack were a custom object — but you used a Python list.
3.Accessing stack[-1] when the stack is empty (causes IndexError).
4.Confusing value vs index in loops (for ele in nums1 gives values, not indices).
5.Building nge with wrong keys (index vs value), then trying to look up by value — mismatch causes errors.

1. So I am using an empty list to create a stack => None means “no object”. Example: x = None. [] means “an empty list object” — it exists, just has length 0.

Checks:

stack is None checks whether the variable points to None. For stack = [], stack is None is False because it holds a list object.
if stack: checks truthiness: empty list → False, non-empty list → True.
So:
stack is not None is True for stack = []. That does not mean the list has elements — it just means the variable points to a list object.
To test “is the list non-empty?” use if stack: or while stack:

So I am using an empty list stack=[] print(stack is None) => False as Output.If I am checking while stack is not None and stack[-1]<=nums2[i] => You will get an ERROR because , 
stack is not None (True because it holds an empty list object) and stack[-1] => This is the error becaus eyou dont have any element in list. 

so you need to check while stack and stack[-1]<=nums2[i] => Python internally checks this while bool(stack): bool([]) => False 
  Empty list → False
  Non-empty list → True
while length_of_stack > 0: (That is exactly what while stack: means for lists)
