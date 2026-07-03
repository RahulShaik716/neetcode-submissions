class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
    //   let arr = [];
    //   for(let i in numbers){
    //     if(numbers[i]>target)
    //     numbers.splice(i,1);
    //   }
    //   for(let i in numbers)
    //   {
    //     let needed  = target - numbers[i];
    //     let index = numbers.indexOf(needed);
    //     if(index > i)
    //     arr.push(numbers[i],numbers[index]);
    //   }
    //   console.log(numbers)
    //   return arr; 
    // }
    //two pointer approach
    let left = 0 ; let right = numbers.length - 1; 
    while(left!=right)
    {
        if(numbers[left] + numbers[right] == target)
        return [left+1,right+1];
        else if(numbers[left]+numbers[right]>target)
        right--
        else 
        left ++;
    }
    return -1;
}
}