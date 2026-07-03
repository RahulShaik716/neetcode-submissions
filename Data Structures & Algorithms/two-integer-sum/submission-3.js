class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hash = new Map();
        for(let i=0;i<nums.length;i++)
        {
            console.log(nums[i])
            console.log(hash.has(target-nums[i]))
            if(hash.has(target-nums[i]))
            return [i,hash.get(target-nums[i])];
            else 
            hash.set(nums[i],i)
        }
    }
    
}
