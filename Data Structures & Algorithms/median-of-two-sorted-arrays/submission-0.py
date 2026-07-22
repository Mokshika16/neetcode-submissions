class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        l, r = 0, m
        half = (m + n + 1) // 2

        while l <= r:
            i = (l + r) // 2
            j = half - i

            nums1Left = nums1[i-1] if i > 0 else float("-inf")
            nums1Right = nums1[i] if i < m else float("inf")

            nums2Left = nums2[j-1] if j > 0 else float("-inf")
            nums2Right = nums2[j] if j < n else float("inf")

            # Correct partition found
            if nums1Left <= nums2Right and nums2Left <= nums1Right:

                # Odd length
                if (m + n) % 2:
                    return max(nums1Left, nums2Left)

                # Even length
                return (max(nums1Left, nums2Left) +
                        min(nums1Right, nums2Right)) / 2

            elif nums1Left > nums2Right:
                r = i - 1

            else:
                l = i + 1