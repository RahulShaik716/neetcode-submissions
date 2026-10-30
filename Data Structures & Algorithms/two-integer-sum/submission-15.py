class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #naive 
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        
        # #time-O(n^2) , space - O(1)

    
        # a = []
        # for i,num in enumerate(nums):
        #     a.append([num,i])
        # a.sort()
        # n = len(nums)
        # l = 0
        # r = n-1

        # while l<r:
        #     sum_ = a[l][0] + a[r][0]

        #     if sum_ == target:
        #         return [min(a[l][1],a[r][1]),max(a[l][1],a[r][1])]
        #     elif sum_ < target:
        #         l = l+1
        #     else:
        #         r = r - 1
        
        # #time - O(n) , space - O(n)

        hash = {}

        for idx,i in enumerate(nums):
            diff = target - i 
            if diff in hash:
                return[hash[diff],idx]
            hash[i] = idx
        
