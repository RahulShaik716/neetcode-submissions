class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        min_ = float("inf")
        while left<=right:
              if nums[left] < nums[right]:
                min_ = min(min_,nums[left])
              mid = (left+right)//2
              min_ = min(min_,nums[mid])
              if nums[mid] >= nums[left]:
                left = mid + 1
              else:
                right = mid - 1
        return min_
            
        