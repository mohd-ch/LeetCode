/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let a = [];
    let i = 1;
    
    while (i <= n) {
        if (i % 3 == 0 && i % 5 == 0) {
            a.push("FizzBuzz");
        } else if (i % 5 == 0) {
            a.push("Buzz");
        } else if (i % 3 == 0) {
            a.push("Fizz");
        } else {
            a.push(i.toString());
        }
        i++;
    }
    
    return a;
};