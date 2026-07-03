class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let arr = new Set();
        if(nums.length<=1)
        return nums.length;
        let max = 1; 
        nums.sort((a,b)=>a-b)
        for(let i=0;i<nums.length;i++)
        {
            if(nums[i+1]==nums[i]+1||nums[i]==nums[i+1]){
            arr.add(nums[i])
            arr.add(nums[i+1])}
            else
            {
                if(max<arr.size)
                max = arr.size; 
                arr.clear();
            }
        }
         if(max<arr.size)
         max = arr.size; 
        return max ;
    }
}
