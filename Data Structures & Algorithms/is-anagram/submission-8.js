class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
       let a1 = [...s]
       let a2 = [...t]
       for(let i of a2)
       {
        if(!a1.includes(i))
        return false; 
        else
        {
           let index = a1.indexOf(i);
           if(index!=-1)
           a1.splice(index,1);
        }
       }
       if(a1.length!=0)return false;
       else
       return true;

    }
}
