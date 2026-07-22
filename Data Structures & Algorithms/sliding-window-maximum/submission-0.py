from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # stores indices
        res = []

        for i in range(len(nums)):
            # Remove indices outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Start adding results once the first window is formed
            if i >= k - 1:
                res.append(nums[q[0]])

        return res