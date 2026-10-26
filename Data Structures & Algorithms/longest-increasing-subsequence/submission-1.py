class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] represents longest increasing sequence possible at index i 
        # dp[i] = max(1, 1+dp[i+1...n])
        # dp[n-1] = 1
        #bottom-up 
        #yes 
        #naive dfs , O(2^n)
        n = len(nums)
        LIS = [1] * n 
        LIS[n-1] = 1
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        
        return max(LIS)


        