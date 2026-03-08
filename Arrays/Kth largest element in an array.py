import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=-(nums[i])
        heapq.heapify(nums) # It will not sort the array , it maintains heap property - maintains small element as root 
        # heap wont delete dupliactes 
        for p in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
# Time Complexity: O(logn) for pop . k times O(klogn) + O(n) for makine negative elements => worst case k==n , O(nlogn) 

Optimized version :

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_new=nums[:k]
        heapq.heapify(nums_new)  
        for num in nums[k:]: # we dont require heapify in for loop - Because heapify() is for when you have an arbitrary array and you want to turn it into a heap from scratch
            if num > nums_new[0]:
                heapq.heappushpop(nums_new, num)

        return nums_new[0]
# Time Complexity: O(n log k)
