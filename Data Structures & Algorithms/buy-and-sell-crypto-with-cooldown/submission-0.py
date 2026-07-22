class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]   # Holding stock
        sold = 0            # Just sold stock
        rest = 0            # Cooldown / no stock

        for price in prices[1:]:
            prevHold = hold
            prevSold = sold
            prevRest = rest

            hold = max(prevHold, prevRest - price)
            sold = prevHold + price
            rest = max(prevRest, prevSold)

        return max(sold, rest)