// REMOVE FIRST AND LAST CHARACTER
// 8KYU

/*
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
*/

function removeChar(str) {
    // return str.slice(1, -1);
    // or 
    str1 = str.split('');
    str1.shift();
    str1.pop();
    return str1.join('');

}

console.log(removeChar('eloquent'))
console.log(removeChar('country'))
console.log(removeChar('person'))
console.log(removeChar('place'))