class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input list of numbers, output : list of products except self 

        #naive i -> 0 to n , j from 0 to i-1 and k from i+1 to n 
        # n = len(nums)
        # output = [0] * n 
        # for i in range(n):
        #     prev = 1 
        #     for j in range(i):
        #         prev *= nums[j]
        #     #O(n)
        #     post  = 1

        #     for j in range(i+1,n):
        #         post *= nums[j]
        #     #O(n)

        #     output[i] = prev * post

        # return output            
        #time - O(n2), instead of doing two scans to the left and right , which are repetitive , we can do one scan for prefix prod and postfix prod , space - O(3n)
        # prod, zero_count = 1,0 
        # #O(n)
        # for num in nums:
        #     if num:
        #         prod *= num 
        #     else:
        #         zero_count += 1
        
        # if zero_count > 1: return [0] * len(nums)
        # output = [0] * len(nums)
        # #O(n)
        # for index,value in enumerate(nums):
        #     if zero_count:
        #         if value:
        #             output[index] = 0 
        #         else:
        #             output[index] = prod
        #     else:
        #         output[index] = prod//value
        
        # return output
        # #division method , time - O(n), space - O(1) , O(n) for output 

        # #prefix and suffix 
        # n = len(nums)
        # prefix=[0] * n 
        # suffix = [0] *n 
        # output = [0] * n 
        # #this is called list multiplication 
        # prefix[0] = 1
        # for i in range(1,n):
        #     prefix[i] = prefix[i-1]*nums[i-1]
        
        # suffix[n-1] = 1
        # for i in range(n-2,-1,-1):
        #     suffix[i] = suffix[i+1]*nums[i+1]
        
        # for i in range(n):
        #     output[i] = prefix[i] * suffix[i]

        # return output
        # #time - O(n) , space - O(3n)

       
        prefix = 1
        n = len(nums)
        output = [0]*n
        for i in range(n):
            output[i] = prefix
            prefix = prefix*nums[i]
            
        suffix = 1
        for i in range(n-1,-1,-1):
            output[i] *= suffix 
            suffix = suffix * nums[i]
        return output


