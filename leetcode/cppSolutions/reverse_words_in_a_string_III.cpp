#include <bits/stdc++.h>

class Solution
{
public:
    string reverseWords(string s)
    {

        // Outputting resultant string
        string result;

        // Initializing last space
        int lastSpaceIndex = -1;
        for (int strIndex = 0; strIndex < s.length(); strIndex++)
        {

            // Stop at every space or at the end of the string
            if ((strIndex == s.length() - 1) || s[strIndex] == ' ')
            {

                // Short hand if else
                int reverseStrIndex = (strIndex == s.length() - 1) ? strIndex : strIndex - 1;
                for (; reverseStrIndex > lastSpaceIndex; reverseStrIndex--)
                {
                    result += s[reverseStrIndex];
                }

                // If it is not the end of the string
                if (strIndex != s.length() - 1)
                {
                    result += ' ';
                }
                lastSpaceIndex = strIndex;
            }
        }
        return result;
    }
};