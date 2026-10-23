class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input : array of numbers (0 - n) , output : missing number (single)
        #edge cases : what if all the numbers are present what would you return then ? 
        #are the numbers in sequence or are the numbers in sorted order ? 
        # i = 0 
        # n = len(nums) + 1
        # #sorting so that all are in order , O(nlogn)
        # nums.sort()
        # #O(n) -> loop
        # while i < n and i<len(nums):
        #     #we are checking for missing number over here 
        #     if i!=nums[i]:
        #         return i
        #     i+=1
        
        # #if we reached the end of array, and have not found anything then return n+1 as missing  
        # return i
        #for this solution, time complexity is O(1)

        #optimization should be O(n)
        # n = len(nums)
        # xor = n 
        # for i  in range(n):
        #     xor ^= i ^ nums[i];

        # return xor 

        # n = len(nums)
        # res = n
        # for i in  range(n):
        #     res+= i - nums[i]  
        # return res
        #res - 2 when i = 0 , when i = 1, res = 1 

        s = set()
        n = len(nums)
        for i in nums:
            s.add(i)
        for i in range(n+1):
            if i not in s:
                return i 
    



        