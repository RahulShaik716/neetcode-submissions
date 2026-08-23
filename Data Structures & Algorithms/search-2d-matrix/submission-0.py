class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [i for j in matrix for i in j]
        left = 0 
        right = len(flattened) - 1

        while left<=right:
            mid = (left+right)//2

            if flattened[mid] == target:
                return True 
            elif flattened[mid] > target:
                right = mid - 1
            else :
                left = mid + 1
        return False