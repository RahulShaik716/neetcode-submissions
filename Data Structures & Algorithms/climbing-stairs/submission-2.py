class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        #s(n) = s(n-1) + s(n-2)
        # we need to start from 2, n  base case : s(1) = 1, s(0) = 1
        if n in self.memo:
            return self.memo[n]

        if n == 0 or n == 1:
            return 1 
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = result
        return result
    
        