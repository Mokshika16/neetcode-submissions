class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack
            subset.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res