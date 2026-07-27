class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        lowest_possible_buy = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - lowest_possible_buy)
            lowest_possible_buy = min(lowest_possible_buy, price)
        
        return max_profit
        