'''

    This is the solution to the leetcode problem "242. Valid Anagram".
    In this file, I go in depth on the processes for the purpose of learning
    more about hashmaps. The link to the problem is provided below:

    https://leetcode.com/problems/valid-anagram/

'''

class Solution:

    def hashmap(self, s: str, t: str) -> bool:
        '''

            In this solution, we create two hashmaps that count the frequencies
            of each character and then compare the two. If they are identical,
            return True, otherwise return False

        '''

        # If the lengths are not equal, they are by intuition not anagrams
        # Further operations would also throw an IndexError given len(s) > len(t)
        if len(s) != len(t):
            return False

        # Creating the two hashmaps
        countS, countT = {}, {}

        # This is the actual counting process, for every character in the string
        # add one to its current value in the hashmap. If it does not exist,
        # create the kay using the .get() function. The first parameter is the key
        # to be created and the second parameter is its initial value
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        # Comparing the two dictionaries
        if countS == countT:
            return True
        return False

    def oneLiner(self, s: str, t: str) -> bool:
        '''

            Sort the strings, if they come out identical return True, otherwise
            return False

        '''
        return True if sorted(s) == sorted(t) else False
