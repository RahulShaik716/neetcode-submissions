class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        min_ = float("inf")
        while left<=right:
            mid = (left+right)//2
            min_ = min(min_,nums[mid],nums[left],nums[right])

            if nums[left] < nums[mid]:
                left = mid+1
            else:
                right = mid -1 
        return min_
            
        