class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        t1={}
        for c in range(len(s)):
            a=s[c]
            b=t[c]
            if a in s1 and s1[a]!=b:
                return False
            if b in t1 and t1[b]!=a:
                return False
            s1[a]=b
            t1[b]=a
        return True

#Time Complexity: O(n) , n is length of string 
# space Complexity: O(n) +O(n)  =>O(n) where n is length of string. sO IF THE QUESTION GUARANTEES THAT IT CONTAINS ONLY ALPHABETS IN ONE CASE THEN SPACE COMPLEXITY IS O(26) =>O(1) 
