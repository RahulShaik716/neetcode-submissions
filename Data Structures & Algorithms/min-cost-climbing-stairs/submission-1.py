class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
          minCostClimbingStairs(n-1) + cost[n-1], minCostClimbingStairs(n-2) + cost[n-2]
          minCost
        """
        n = len(cost)
        dp = [0] * (n+1)
        dp[0] = 0 
        dp[1] = 0 

        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        
        return dp[n]