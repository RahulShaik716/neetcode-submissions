class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx={}
        for idx,i in enumerate(nums): 
            diff = target - i
            if diff in val_idx:
                return [val_idx[diff],idx]
            else:
                val_idx[i] = idx
            