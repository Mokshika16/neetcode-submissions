class Solution:
    def permute(self, nums):
        res = []
        perm = []
        used = set()

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for num in nums:
                if num in used:
                    continue

                perm.append(num)
                used.add(num)

                dfs()

                perm.pop()
                used.remove(num)

        dfs()
        return res