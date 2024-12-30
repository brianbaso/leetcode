class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of total profit
        # iterate through prices with i, j
            # if theres opportunity for profit, add it to total and continue
        # return total profit
        total = 0
        for i in range(0, len(prices) - 1):
            currDiff = prices[i+1] - prices[i]
            if currDiff > 0:
                total += currDiff
        return total




