class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        maxP = 0
        while r < len(prices) - 1:
            if prices[l] <= prices[r]:
                r += 1
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
        return maxP