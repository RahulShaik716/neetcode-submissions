class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input : array of numbers (0 - n) , output : missing number (single)
        #edge cases : what if all the numbers are present what would you return then ? 
        #are the numbers in sequence or are the numbers in sorted order ? 
        i = 0 
        n = len(nums) + 1
        nums.sort()
        while i < n and i<len(nums):
            if i!=nums[i]:
                return i
            i+=1
        
        return i