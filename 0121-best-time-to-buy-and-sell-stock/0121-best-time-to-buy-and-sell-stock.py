class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            lowest = min(lowest,prices[i])
            profit = prices[i] - lowest
            max_profit = max(max_profit,profit)
        return max_profit