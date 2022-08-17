'''

    This is the solution to the leetcode problem "49. Group Anagrams".
    In this file, I go in depth on the processes for the purpose of learning
    more about hashmaps. The link to the problem is provided below:

    https://leetcode.com/problems/group-anagrams/

'''

class Solution:

    def hashmap(self, strs: List[str]) -> List[List[str]]:
        '''

            In this solution, we create a hashmap to group the different
            anagrams, with the key values being the sorted string in the
            list strs and the values being the respective anagrams of the
            keys.

            We must use a tuple since lists are not hashable, therefore
            they cannot be used as keys. This is due to the fact that lists
            are mutable. By that logic, we could also use strings if we wanted
            to because they are, like tuples, immutable.

        '''

        # Creating the hashmap
        hashmap = {}

        # If the key does not exist, appending to the current key would
        # throw a key error, so if it does not already exist, create the
        # key and give it an array with the anagram.
        for s in strs:
            if tuple(sorted(s)) not in hashmap:
                hashmap[tuple(sorted(s))] = [s]
            else:
                hashmap[tuple(sorted(s))].append(s)

        # Return the grouped anagrams
        return hashmap.values()

    def counting(self, strs: List[str]) -> List[List[str]]:
        '''

            In this solution, we use a frequency counter, similar to the
            method used in the valid anagrams problem, to map each anagram
            with their respective keys. We know that the characters are going
            to be from lowercase a to z so we only need to create an array of
            size 26 in order to keep a proper count of each character within
            a string.

        '''
        # This creates a dictionary that has lists as values
        ans = collections.defaultdict(list)

        for s in strs:
            # This list count holds the frequency of each character
            count = [0] * 26

            '''

                Essentially, the ord(c) - ord("a") rescales the ascii values from
                a to z down to 0 to 25. The indices in the array count only go
                up to 25 so if we were to use the default ascii values, it would
                very quickly throw an IndexError. The for loop finds the
                index that corresponds to the character and adds one to it;
                this part of the code is the frequency counter

            '''
            for c in s:
                count[ord(c) - ord('a')] += 1

            # If the string has a count similar to that of one of the keys,
            # append it to the respective list
            ans[tuple(count)].append(s)

        return ans.values()
