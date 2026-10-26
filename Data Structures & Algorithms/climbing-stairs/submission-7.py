class Solution:
    def climbStairs(self, n: int) -> int:
        #each dp[i] represents no of steps required to reach step i 
        # recurrence relation, dp [i] = dp[i-1] + dp[i-2]

        #dp[0] = 1, dp[1] = 1 , bottom-up , optimize from using  first, second 

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        