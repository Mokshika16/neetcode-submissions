class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            l, r = 0, len(lis)

            while l < r:
                mid = (l + r) // 2

                if lis[mid] < num:
                    l = mid + 1
                else:
                    r = mid

            if l == len(lis):
                lis.append(num)
            else:
                lis[l] = num

        return len(lis)
        