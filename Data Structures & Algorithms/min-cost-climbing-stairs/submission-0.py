class Solution:
    def minCostClimbingStairs(self, cost):

        one = 0   # cost to reach step i-1
        two = 0   # cost to reach step i-2

        for i in range(2, len(cost) + 1):

            current = min(
                one + cost[i-1],
                two + cost[i-2]
            )

            two = one
            one = current

        return one     