'''

    This is the solution to the leetcode problem "485. Max Consecutive Ones".
    In this file, I go in depth on the processes for the purpose of learning
    more about arrays. The link to the problem is provided below:

    https://leetcode.com/problems/max-consecutive-ones/

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''

            In this solution, we simply pass through the array and check
            to see if the element is equal to 1. If it is, then add one to
            the count, else, compare the count and the max_count and take the
            maximum of the two and bring the count back to zero as the streak is
            broken. Return the larger of the two.

        '''
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)
