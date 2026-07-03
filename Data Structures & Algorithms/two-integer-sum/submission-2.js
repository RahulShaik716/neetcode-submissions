class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for(let i=0;i<nums.length;i++)
        {
            let elem = target-nums[i];
            let index = nums.indexOf(elem);
            if(index!=-1 && i!=index)
            {
                if(index>i)
                return [i,index]
                else
                return [index,i]
            }
        }
       
    }
}
