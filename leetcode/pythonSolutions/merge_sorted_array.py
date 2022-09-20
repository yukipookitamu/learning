'''

    This is the solution to the leetcode problem "88. Merge Sorted Array".
    In this file, I go in depth on the processes for the purpose of learning
    more about arrays. The link to the problem is provided below:

    https://leetcode.com/problems/merge-sorted-array/

'''

class Solution:

    def mergeAndSort(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''

            In this solution, we simply take the elements from nums2 and add
            them after the m index on nums1. From there we sort the elements
            to ensure that they are in non-decreasing order.

        '''

        # We iterate from m to m+n to focus on the zeros that follow the
        # mth element
        for i in range(m,m+n):

            # i-m should correctly iterate through the elements in nums2 up
            # to n times
            nums1[i] = nums2[i-m]

        nums1.sort()

    def threePointer(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''

            In this solution, the algorithm has a time complexity O(m+n),
            which is better than the logarithmic time complexity of the merge
            and sort method mentioned above. In this solution, we use three
            pointers: p1 for nums1_copy, p2 for nums2, and p for nums1.

        '''
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1

    def threePointerBackwards(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''

            In this solution, we iterate backwards to make the process easier.
            Rather than going from beginning to end, we simply iterate backwards
            and assign the last index the larger element.

            In most sorting problems, it helps to think of iterating through
            the problem backwards.

        '''

        # The pointers start at the 'end' of each array
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # We iterate backwards, having the largest element added to the end
        # of the array nums1
        for i in range(m+n-1, -1, -1):

            # Assigning the last index of p1 the larger element
            if p2 < 0 or (nums1[p1] > nums2[p2] and p1 >= 0):
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
