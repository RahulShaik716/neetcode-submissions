class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        start = prices[0] 
        for end in prices[1:]:
            if end<start:
                start = end
            else:
                profit = end-start
                max_profit = max(profit,max_profit)
        return max_profit