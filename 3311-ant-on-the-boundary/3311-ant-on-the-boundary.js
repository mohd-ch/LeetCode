/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    let pos = 0;
    let count = 0;
    for(i = 0; i < nums.length; i++){
        pos = pos + nums[i];
        if(pos === 0){
            count++
        }
        }
    return count  
};