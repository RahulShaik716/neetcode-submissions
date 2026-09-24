class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin,currMax = 1,1 
        res  = max(nums)
        for n in nums: 
            tmp = currMax*n
            currMax = max(n*currMax,n*currMin, n)
            currMin = min(tmp,n*currMin, n)
            res = max(res,currMax)
        return res
        