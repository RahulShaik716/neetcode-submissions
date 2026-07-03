class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prefix = [];
        prefix[0] =1;
        let len = nums.length; 
        let postfix = [];
        postfix[len-1] = 1;
        for(let i =1;i<nums.length;i++)
        {
            prefix[i] = nums[i-1]*prefix[i-1]; 
        }
        for(let i=nums.length-2;i>=0;i--)
        {
            postfix[i] = nums[i+1]*postfix[i+1];
        }
        let output = [];
        for(let i=0;i<len;i++)
        output[i] = prefix[i]*postfix[i];
        return output;
    }
}
