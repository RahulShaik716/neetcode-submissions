class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set()
        for i in nums:
            if i not in n:
                n.add(i)
            else:
                return True
        return False
        