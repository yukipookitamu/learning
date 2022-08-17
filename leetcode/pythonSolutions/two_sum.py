'''

    This is the solution to the leetcode problem "1. Two Sum".
    In this file, I go in depth on the processes for the purpose of learning
    more about hashmaps. The link to the problem is provided below:

    https://leetcode.com/problems/two-sum/

    Note: in the hasmap solutions, the keys are the numbers and the values are
    the indices (for example: nums = [4,0,9,1]; hashmap = {4:0, 0:1, 9:2, 1:3})

'''

class Solution:

    def brute(self, nums: List[int], target: int) -> List[int]:
        '''

            This is a brute force solution to the two sum problem.
            In this solution, we use two pointers to iterate through
            the elements in the list nums. We simply add the two
            numbers that each pointer iterates through until we find
            the numbers that add up to our target, then we return
            the indices for those numbers.

        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        '''

            This solution has a time complexity O(n^2) and a space complexity
            O(1)

        '''

    def twoPass(self, nums: List[int], target: int) -> List[int]:
        '''

            In this solution, we use a hashmap as rather than
            searching in O(n) time like an array would, we are
            able to search in O(1), given that there are no
            collisions.

        '''

        # Creating the hashmap
        hashmap = {}

        # Adding elements to the hashmap, would this not take extra time O(n)?
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        # Searching thorugh the hashmap to find the complement
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        '''

            This solution passes twice, giving us a time complexity of O(2n)
            which simplifies to O(n). The space complexity is slightly worse
            than the first solution with O(n).

        '''

    def onePass(self, nums: List[int], target: int) -> List[int]:
        '''

            In the single pass solution, we simultaneously iterate
            through the list and check to see if the complement exists.
            If the complement exists in the hashmap, we return our
            current index as well as the index of the complement which
            should be stored as a value of its respective key.

        '''
        # Creating the hashmap
        hashmap = {}

        # Looping through elements in list; if the complement already exists
        # in the list, then return its index as well as the current number
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

        '''

            Similar to the two pass solution, the time complexity is O(n) and
            the space complexity is O(n). This is the optimal solution.

        '''
