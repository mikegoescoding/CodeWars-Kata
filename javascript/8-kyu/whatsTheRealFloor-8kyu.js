// WHAT'S THE REAL FLOOR?
// 8 KYU

/*
Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor ('cause of superstition).

Write a function that given an American floor (passed as an integer) returns the real floor.
Moreover, your function should work for basement floors too: just return the same value as the passed one.

Usage Examples
getRealFloor(1) == 0 
getRealFloor(0) == 0 // Special case to please Europeans
getRealFloor(5) == 4
getRealFloor(15) == 13
getRealFloor(-3) == -3
*/

function getRealFloor(n) {
  if (n === 0 || n < 0) return n
  if (n < 13) return n - 1
  if (n > 13) return n - 2
  if (n === 13) return "This floor does not exist in America!"
}

console.log(getRealFloor(1)) // 0
console.log(getRealFloor(5)) // 4
console.log(getRealFloor(15)) // 13
console.log(getRealFloor(0)) // 0
console.log(getRealFloor(-3)) // -3
console.log(getRealFloor(13)) // "This floor does not exist in America!"