'''

    This is the solution to the leetcode problem "977. Squares of a Sorted Array".
    In this file, I go in depth on the processes for the purpose of learning
    more about arrays and pointers. The link to the problem is provided below:

    https://leetcode.com/problems/squares-of-a-sorted-array/

'''

class Solution:

    def sorting(self, nums: List[int]) -> List[int]:
        '''

            In this solution, we take advantage of the built-in sort method
            to successfully sort all the sqaures. We simply take the sqaure
            of each number in the list nums and add it to a array 'res'. Once
            we add all the squares to the new array, we use the sort method
            to sort all the squares in a non-decreasing order.

        '''

        # Creating an array
        res = []

        # Iterating through each number in the list and squaring it
        for num in nums:
            res.append(num*num)

        # Sorting the elements
        res.sort()
        return res

    def twoPointer(self, nums: List[int]) -> List[int]:
        '''

            In this solution, we use a bit of intuition to solve the problem.
            Something to not is that the array nums is given to us an a
            non-decreasing order. For example, in the array:

            [-7, -5, 2, 3, 4]

            The elements are increasing from left to right. With this, we can
            see that the largest square will always reside at one of the edges.
            For this we use two pointers, one at the left and one at the right.
            We compare the absolute values of the leftmost and rightmost elements
            and have the larger of the two be added to the end of the resultant
            array, adding elements from right to left.

        '''

        n = len(nums)
        left = 0
        right = n-1

        # Here we create an array with length n to allow us to put elements
        # add the end. if we attempt to add elements starting from the end
        # with a normal array, we'd get an IndexError
        res = [0] * n

        # Interate backwards from len(nums) - 1 to -1, backwards
        for i in range(n-1, -1, -1):

            # Comparison process, set larger value to end
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] * nums[left]
                left += 1
            else:
                res[i] = nums[right] * nums[right]
                right -= 1

        return res
