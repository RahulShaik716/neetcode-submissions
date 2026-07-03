class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
       let left = 0 ;
       let count = new Map(); 
       let max = 0; 
       for(let right=0;right<s.length;right++)
       {
         count.set(s[right] , 1 + (count.get(s[right]) || 0))
         while(((right-left+1)-Math.max(...count.values())) > k)
         {
            count.set(s[left],count.get(s[left])-1);
            left+=1
         }
         max = Math.max(max, right-left+1)
       }
       return max;     
    }
}
