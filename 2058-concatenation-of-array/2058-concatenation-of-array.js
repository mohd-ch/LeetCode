/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    ans = nums.slice()
    for(i = 0; i< nums.length; i++){
        ans.push(nums[i])
    }
    return ans 
};