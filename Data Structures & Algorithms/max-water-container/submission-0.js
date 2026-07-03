class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        //two pointer again.. 
        let left = 0; let right  = heights.length-1; let max = -Infinity; 
        let width; let height; 
        while(left!=right)
        {
             width = right-left; 
             height = Math.min(heights[left],heights[right])
             max = Math.max(max,width*height)
             if(heights[left]<heights[right])
             left++; 
             else
             right--;
        }
        return max;
    }
}
