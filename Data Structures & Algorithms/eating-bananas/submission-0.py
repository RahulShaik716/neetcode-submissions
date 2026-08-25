class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeTaken(rate):
            total = 0 
            for i in piles:
                total += (i + rate - 1)//rate; 
            
            return total 
        
        l,r = 1, max(piles)

        while l<r:
            mid = (l+r)//2

            if timeTaken(mid)>h:
                l = mid + 1
            else:
                r = mid
        
        return l