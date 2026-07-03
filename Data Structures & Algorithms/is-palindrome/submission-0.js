class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
       s = s.replace(/\W/g,"").toLowerCase();
       let ns = s.split('').reverse().join('');
       console.log(s,ns);
       return s==ns;
    }
}
