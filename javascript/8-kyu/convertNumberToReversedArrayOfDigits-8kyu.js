// CONVERT NUMBER TO REVERSED ARRAY OF DIGITS
// 8 KYU

/*
Convert number to reversed array of digits
Given a random number:

You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
*/

// function digitize(n) {
//     return string(n).split("").reverse().join('')
// }
function digitize(n){
	//converts n to string 
    return n.toString()
    //splits it into an array
    .split('')
    //reverses the order
    .reverse()
    //converts each element into integer
    // parseInt() // <--- works, but not best solution
    .map(Number)
    // one line, below
    //return n.toString().split('').map(Number).reverse();
}
console.log(digitize(35231))
console.log(digitize(912383217123632))