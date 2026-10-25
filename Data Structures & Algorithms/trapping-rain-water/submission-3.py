class Solution:
    def trap(self, height: List[int]) -> int:
        # list of +ve integers is the input, output : total amount of water trapped b/w the bars, 
        #each value represents the height of the bar . each bar has width 1 , 
        # take each bar , caluculate left max and right max , total = min (leftmax,rightmax) - height of the bar itself 

        # total = 0 
        # n = len(height)

        # for i in range(n):
        #     leftMax,rightMax = height[i],height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax,height[j])

        #     for j in range(i+1,n):
        #         rightMax = max(rightMax,height[j])
            
        #     total += min(rightMax,leftMax) - height[i]
        
        # return total
        # #time - O(n2) , space - O(1)

        n = len(height)
        leftMax = [0] * n 
        rightMax = [0] * n 

        leftMax[0] = height[0]
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])

        rightMax[n-1] = height[n-1]

        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        total = 0 
        for i in range(n):
            total+= min(leftMax[i],rightMax[i]) - height[i]
        
        return total


