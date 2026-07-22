class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robRange(nums):
            prev2 = 0
            prev1 = 0

            for money in nums:
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr

            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]

        # Case 1: Rob houses 0 to n-2
        # Case 2: Rob houses 1 to n-1
        return max(robRange(nums[:-1]), robRange(nums[1:]))