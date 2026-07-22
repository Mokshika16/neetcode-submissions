class Solution:
    def combinationSum(self, nums, target):
        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur[:])
                return

            if i == len(nums) or total > target:
                return

            # Include nums[i]
            cur.append(nums[i])
            dfs(i, total + nums[i])

            # Exclude nums[i]
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res