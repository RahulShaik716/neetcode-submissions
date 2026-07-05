class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for j,i in enumerate(nums):
            diff = target - i
            if diff in h:
                return [h[diff],j]
            h[i] = j