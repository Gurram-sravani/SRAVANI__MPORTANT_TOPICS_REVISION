class Permutation:
    def permutation_in_array(self, nums):
        n = len(nums)
        output = []
        path = []
        used = set()
        self.backtrack(nums, n, output, path, used)
        return output

    def backtrack(self, nums, n, output, path, used):
        if len(path) == n:
            output.append(path.copy())
            return

        for i in range(n):
            if i in used:
                continue

            # choose
            used.add(i)
            path.append(nums[i])

            # explore
            self.backtrack(nums, n, output, path, used)

            # un-choose
            path.pop()
            used.remove(i)
# Time complexity: n!*n
# Space Complexity: used O(n) + path O(n) =>O(2n) 

Optimized Approach: In this approach, I am not using any used array to store the index

