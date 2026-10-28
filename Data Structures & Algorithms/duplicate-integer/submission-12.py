class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input : array of nums, output : boolean 
        # need to check if the number appears more than once or not 
        #if duplicate return True, if not False

        # #naive 

        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] == nums[j]:
        #             return True 

        
        # return False
        # #time - O(n2), space - O(1)

        #optimization - use hashmap or set , coz we are traversing the same number mutliple times . 

        existing = set() 
        for i in nums:
            if i in existing:
                return True
            existing.add(i)
        return False