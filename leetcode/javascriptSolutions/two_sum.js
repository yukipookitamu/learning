/*

  This is the beginnning of my journey for learning Javascript

  This problem is the classic two sum problem. We find two numbers
  in an array that add up to the "target" number. There are two ways
  that I will go about this problem:

  1. Brute Force Method: Search through all the elements in pairs and
     find the sum

  2. Hashmap: Searching through a hashmap is faster, we iterate through
     the elements and if the complement already exists, we return the result

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var bruteForce = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i,j];
            }
        }
    }
};
