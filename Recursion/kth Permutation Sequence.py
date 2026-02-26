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
