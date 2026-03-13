class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        total=0
        n=len(s)
        i=0
        memo=[-1]*n
        return self.decode(s,n,i,memo)
    def decode(self,s,n,i,memo):
        if i==n:
            return 1
        if s[i] == '0':
            return 0
        if memo[i]!=-1:
            return memo[i]
        ways=self.decode(s,n,i+1,memo)
        if i+1<n:
            take=int(s[i:i+2])
            if take>=10 and take<=26:
                ways+=self.decode(s,n,i+2,memo)
        memo[i]=ways
        return ways

