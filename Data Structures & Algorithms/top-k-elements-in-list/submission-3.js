class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
       let h = new Map(); 
       for(let i of nums)
       {
        if(!h.has(i))
        h.set(i,1);
        else
        h.set(i,h.get(i)+1);
       }
       let sorted = [...h].sort(([i1,v1],[i2,v2])=>{
        return v2-v1
       })
       console.log(sorted)
       let a = [];
       for(let i=0;i<k;i++)
       a.push(sorted[i][0]);
       return a;
    }
}
