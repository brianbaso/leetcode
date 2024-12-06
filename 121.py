class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, minimum_price = 0, prices[0]
        for price in prices:
            if price < minimum_price:
                minimum_price = price
            if price - minimum_price > max_profit:
                max_profit = price - minimum_price
        return max_profit
