'''

    This is the solution to the leetcode problem "3. Longest Substring Without
    Repeating Characters". In this file, I go in depth on the processes for the
    purpose of learning more about hashmaps. The link to the problem is provided
    below:

    https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''

class Solution:

    def brute(self, s: str) -> int:
        '''

            This is the brute force solution for the longest substring
            problem. In this solution, we iterate through all the possible
            substrings while ensuring each is unique. Each substring runs
            through the check function to check for uniqueness; if unique,
            return true, else return false.

        '''

        def check(start, end):

            # Initializing the hashset
            chars = set()

            # Check the characters in the given indices for uniqueness
            for i in range(start, end + 1):
                if s[i] in chars:
                    return False
                chars.add(s[i])
            return True

        # length of longest substring
        res = 0

        # Iterates through each possible substring in s and checks for uniqueness
        # If the substring is unique, take its length and compare it, otherwise
        # restart the loop.
        for i in range(len(s)):
            for j in range(i, len(s)):
                if check(i, j):
                    res = max(res, j - i + 1)

        return res
