class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
     if(strs.length==0)return null;
     let str = strs.join(':;');
     console.log('encode',str);
     return str; 
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
      console.log('decode string=',str);
      if(str == null) return [];
      let arr = str.split(':;');
      console.log('decode array=',arr);
      return arr;
    }
}
