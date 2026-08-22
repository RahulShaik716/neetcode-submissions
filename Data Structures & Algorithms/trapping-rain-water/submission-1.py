class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        lmax = height[0]
        rmax = height[right]

        total = 0 

        while left < right : 
            if lmax <= rmax:
                left += 1
                if lmax<= height[left]:
                    lmax = height[left]    
                else : 
                    total+= lmax - height[left]
            else:
                right-=1
                if rmax <= height[right]:
                    rmax = height[right]
                   
                else:
                    total+= rmax - height[right]
        
        return total 

        

        