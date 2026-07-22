class Solution:
    def climbStairs(self, n):

        one = 1   # ways to reach step 1
        two = 1   # ways to reach step 0

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one