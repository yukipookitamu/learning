'''

    This is the solution to the leetcode problem "125. Valid Palindrome".
    In this file, I go in depth on the processes for the purpose of learning
    more about two pointers. The link to the problem is provided below:

    https://leetcode.com/problems/valid-palindrome/

'''


class Solution:

    '''

        This solution solves the problem WITHOUT the use of any libraries.
        First we make all letters in the string lowercase for easier ASCII
        code values and then we remove all punctuation. With this complete,
        we can now actually incorporate the two pointer technique.

        If we sacrifice some O(n) memory, we can achieve an O(2n) solution 
        which simplifies to O(n). 

    '''

    def isPalindrome(self, s: str) -> bool:

        s = s.lower()  # Minimize ASCII code range

        testStr = ''

        for i in range(len(s)):

            # Checks to see if they are letters
            if ((ord(s[i]) >= 97) and (ord(s[i]) <= 122)) or ((ord(s[i]) >= 48) and (ord(s[i]) <= 57)):
                testStr += s[i]

        left = 0
        right = len(testStr) - 1
        print(testStr)
        while left <= right:

            if (not (testStr[left] == testStr[right])):
                return False
            left += 1
            right -= 1

        return True
