'''

    This is the solution to the leetcode problem "167. Two Sum II - Input Array
    Is Sorted". In this file, I go in depth on the processes for the purpose of
    learning more about hashmaps and pointers. The link to the problem is
    provided below:

    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

'''

class Solution:

    def twoPointer(self, numbers: List[int], target: int) -> List[int]:
        '''

            Here we take advantage of the fact that the array is sorted. We
            use the two pointer technique to point at two elements in the array:
            the largest and the smallest value. Should the sum of the two values
            be less than the target, we incrememnt the left pointer by one to
            increase the value. Otherwise, decrement the right pointer to lower
            the value.

        '''
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right] # sum

            if s == target:
                return [left + 1, right + 1]

            if s < target:
                left += 1

            else:
                right -= 1
