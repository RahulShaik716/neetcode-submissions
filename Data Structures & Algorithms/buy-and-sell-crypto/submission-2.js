class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
           let left = 0; 
           let right = left+1; 
           let max = 0;
           while(right<prices.length)
           {
              let diff = prices[right]-prices[left];
              if(diff<=0) {left = right; right = left+1;continue;}
              max = Math.max(diff,max);
              right++;
           }
return max;
    }
}
