class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx,i in enumerate(nums):
            diff = target - i
            if diff in hash:
                return [hash[diff],idx]
            else:
                hash[i] = idx
        
            