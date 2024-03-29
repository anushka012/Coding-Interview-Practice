class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        
        for i in range(1, len(prices)):
            profit = max(0, profit + prices[i] - prices[i - 1])
            max_profit = max(max_profit, profit)
        
        return max_profit