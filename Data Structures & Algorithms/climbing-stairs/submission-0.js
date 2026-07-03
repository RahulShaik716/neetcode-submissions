class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let count = 0; 
        let res = this.recursive_count(n, count);
        return res; 
    }
    recursive_count(n,count)
    {
        if(n==count)
        return 1; 
        if(count>n)
        return 0; 
        
        return this.recursive_count(n,count+1) + this.recursive_count(n, count+2)
    }
}
