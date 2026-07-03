class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
       let results = new Set(); let left ; let right;
       nums.sort((a,b)=>a-b);
       for(let i=0;i<nums.length;i++)
       {
              left = i+1; right = nums.length-1; 
              while(left<right)
              {
              if(nums[i]+nums[left]+nums[right]==0)
              {results.add(JSON.stringify([nums[i],nums[left],nums[right]])); left++;right--;}
              else if(nums[i]+nums[left]+nums[right]>0)
              right--;
              else 
              left++;
              }
       }
       let array = [];
       results.forEach(x=>{
           array.push(JSON.parse(x))}
       )
        return array;
    }
   
}
