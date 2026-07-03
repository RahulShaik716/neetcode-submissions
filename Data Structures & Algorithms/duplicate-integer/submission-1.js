class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hash = [];
        for(let i of nums)
        {
            if(hash[i]==true)
            return true; 
            else
            hash[i] = true;
        }
        return false;
    }
}
