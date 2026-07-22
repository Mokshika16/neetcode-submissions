class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n

        for i, num in enumerate(nums):
            ans ^= i
            ans ^= num

        return ans