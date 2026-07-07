class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #pre and post mulitplication i guess 
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(len(nums)): 
            pre[i] = nums[i-1] * pre[i-1] if i-1 >= 0 else 1
        
        for i in range(len(nums)-1,-1,-1):
            post[i] = nums[i+1] * post[i+1] if i+1 <= len(nums) -1 else 1
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res