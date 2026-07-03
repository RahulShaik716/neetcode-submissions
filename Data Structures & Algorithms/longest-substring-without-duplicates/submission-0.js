class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let set = new Set(); 
        let l = 0; let max = 0; 
        for(let i of s)
        {
            while(set.has(i))
            {
                set.delete(s[l]);
                l++; 
            }
            set.add(i);
            max = Math.max(max,set.size);
        }
        return max; 
    }
    
}
