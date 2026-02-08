class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1])%2!=0:
            return num
        largest_odd=-1
        left=0
        right=0
        while right<len(num):
            if int(num[right])%2!=0:
                new_str=num[left:right+1]
                #print(new_str)
                largest_odd=max(largest_odd,int(new_str))  
                #print(largest_odd)
            right+=1
        if largest_odd==-1:
            return ""
        else:
            return str(largest_odd)
          
''' If the given string is huge , " int(new_str) " will THROW AN ERROR: ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 4302 digits; 
  use sys.set_int_max_str_digits() to increase the limit
    largest_odd=max(largest_odd,int(new_str))
So try to solve the problem as a string , dont convert into an INT. '''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1])%2!=0:
            return num
        for r in range(len(num)-1,-1,-1):
            if int(num[r])%2!=0:
                return num[:r+1]
        return ""

# Time complexity: O(n) 
# Space Complexity:O(1)


