if you generate all the permutation and sort the output and get the kth permutation string will take more time 

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        path = []
        used = set()

        self.count = 0
        self.answer = None

        self.backtrack(n, path, used, k)

        return self.answer

    def backtrack(self, n, path, used, k):
        # Base case
        if len(path) == n:
            self.count += 1

            if self.count == k:
                self.answer = "".join(map(str, path))
                return True   # stop recursion

            return False

        for i in range(1,n+1):
            if i in used:
                continue
            # choose
            used.add(i)
            path.append(i)

            # explore
            if self.backtrack( n, path, used, k):
                return True   # propagate stop upward

            # un-choose
            path.pop()
            used.remove(i)

        return False

# time complexity : Recursion O(n!.n) 
# Space Complexity : O(n) Recursion Stack Space + O(n) (path+used) + O(n) Output string =>O(n) 

Optimised Version :  In optimized approach, for example n=4 =>[1,2,3,4] , k=17 If I take 0-based  indexing, k=17-1=> you need 16th Permutation 
1+[2,3,4] => here I can form 6 permutations 3!=>6 (0-5) 
2+[1,3,4] => (6-11) permutations
3+[1,2,4] => (12-17) -> 16th Permutation lies in this bucket, but here you can form 6 permutations => 16%6=4 
Finally you need to find 4th Permutation in this bucket our k becomes 4 mathematically (first digit - 3) 
4+[1,2,3] => (18-23)

Now if you take 3+[1,2,4]:
1+[2,4] => again 2 permutations - [0-1] - 0
2+[1,4] => 2 permutation - [2-3] - 1
4+[1,2] => 2 permutations -[4-5] - 2 => k=4/2 =>2  (second digit is 4 => [3,4,-,-]
Now my k becomes 4%2=0 , k=0  and the remaninign set is [1,2]
1+ [2] => 1 permutation -[0]
2+[1] => 1 permutation - [1] 
