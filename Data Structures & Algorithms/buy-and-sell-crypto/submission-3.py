class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        start = 0 
        for end in range(1,len(prices)):
            if prices[end] < prices[start]:
                start = end
                continue
            profit = prices[end] - prices[start]
            max_profit = max(profit,max_profit)
        return max_profit