class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt=0
        result=""
        for c in s:
            if c=='(' and cnt>0:
                result+=c
                cnt+=1
            elif c==')' and cnt>1:
                cnt-=1
                result+=c
                
            elif c==')' and cnt==1:
                cnt-=1
            else:
                cnt+=1
                
        return result

# Time complexity:O(n) , where n is the length of the string 
# Space Complexity :O(1)
