/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    let current = 0
    let maxDepth = 0
    for(let char of s){
        if (char === '('){
            current++
            maxDepth = Math.max(maxDepth, current)
        }
        else if(char === ')'){
            current--
        }
    }
    return maxDepth
};