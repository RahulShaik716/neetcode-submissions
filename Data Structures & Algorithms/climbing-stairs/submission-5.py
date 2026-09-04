class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        #s(n) = s(n-1) + s(n-2)
        # we need to start from 2, n  base case : s(1) = 1, s(0) = 1
        # if n in self.memo:
        #     return self.memo[n]

        # if n == 0 or n == 1:
        #     return 1 
        # result = self.climbStairs(n-1) + self.climbStairs(n-2)
        # self.memo[n] = result
        # return result

        # dp=[0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        prev = 1
        curr = 1
        next_ = 1
        for i in range(2,n+1):
            next_ = prev + curr
            prev = curr
            curr = next_
            
        return next_
        