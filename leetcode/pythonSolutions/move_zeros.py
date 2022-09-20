'''

    This is the solution to the leetcode problem "283. Move Zeros".
    In this file, I go in depth on the processes for the purpose of learning
    more about arrays. The link to the problem is provided below:

    https://leetcode.com/problems/move-zeroes/

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''

            In this solution, we use a two pointer approach, with one pointer
            iterating normally through the elements of the array and the other
            only moving when the elemnt is not equal to zero. Essentially we
            assign all the non-zero elements to the front of the array and make
            the last 'len(nums) - i'th elements zero.

        '''
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        for k in range(i,len(nums)):
            nums[k] = 0
