class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                currMax, currMin = currMin, currMax

            currMax = max(nums[i], currMax * nums[i])
            currMin = min(nums[i], currMin * nums[i])

            res = max(res, currMax)

        return res