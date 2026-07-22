class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxWater = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            maxWater = max(maxWater, width * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater
        