// REVERSED STRINGS
// 8KYU

/*
Complete the solution so that it reverses the string value passed into it.

solution('world'); // returns 'dlrow'
*/


function solution(str) {
    return str.split("").reverse().join('')
}

console.log(solution('world'))
console.log(solution('Hello'))
console.log(solution('Practice'))
console.log(solution('makes'))
console.log(solution('you get better!'))