class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx,i in enumerate(nums):
            j = target-i 
            if j in hash:
               return[hash[j],idx]
            hash[i] = idx
        