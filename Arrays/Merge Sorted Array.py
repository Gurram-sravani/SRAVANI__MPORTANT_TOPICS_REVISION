class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]
                nums1[i]=nums2[j]
                i-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1
# Time Complexity: O(m+n)
#Space Complexity: O(1)



import math
def merge(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = math.ceil((n + m) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < (n + m):
            
            # Case 1: both pointers in arr1
            if i < n and j < n:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < n and j >= n:
                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

            # Case 3: both in arr2
            else:
                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

# Example
arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]

merge(arr1, arr2)

print(arr1)
print(arr2)
