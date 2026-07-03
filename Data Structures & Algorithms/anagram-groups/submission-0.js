class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let anagrams = [];
        let arr = [];
        for(let i of strs)
        {
            let s = i.split(''); 
            s.sort(); 
            console.log(s);
            if(!anagrams[s])
            anagrams[s] = [i];
            else
            anagrams[s].push(i);
        }
        Object.keys(anagrams).forEach(x=>
        arr.push(anagrams[x]));
        return arr;
    }
}
