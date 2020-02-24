// FIND THE SMALLEST INTEGER IN THE ARRAY
// 8 KYU


/*
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
*/


//1 - WORKS! THANK YOU SPREAD :)
class SmallestIntegerFinder {
    findSmallestInt(args) {
      return Math.min(...args)
    }
  }
  
  //2
  // class SmallestIntegerFinder {
  //   findSmallestInt(args) {
  //   var temp  ;
   
  //     for (var i=0;i<args.length;i++){
  //         if(args[i]<=args[0]){
  //             args[0]  = args[i];    
  //             temp = args[i];
  //         }
  //       }
  //     return temp;
  //   }
  // }
  
  // JUST FOR TESTING OUTPUT, IGNORE BELOW
  var justForTesting = new SmallestIntegerFinder();
  console.log(justForTesting.findSmallestInt([78,56,232,12,8])) // 8
  console.log(justForTesting.findSmallestInt([78,56,232,12,18]))  // 12
  console.log(justForTesting.findSmallestInt([78,56,232,412,228])) // 56
  console.log(justForTesting.findSmallestInt([78,56,232,12,0])) // 0
  console.log(justForTesting.findSmallestInt([1,56,232,12,8])) // 1
  