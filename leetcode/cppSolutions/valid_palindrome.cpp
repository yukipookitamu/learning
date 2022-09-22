#include <bits/stdc++.h>

class Solution
{
public:
    bool isPalindrome(string s)
    {
        // convert string to back to lower case
        for (int i = 0; i < s.size(); ++i)
        {
            s[i] = tolower(s[i]);
        }
        int left = 0;
        int right = s.size() - 1;
        while (left < right)
        {
            if (!isalnum(s[right]))
            {
                --right;
            }
            else if (!isalnum(s[left]))
            {
                ++left;
            }
            else if (s[left] != s[right])
            {
                cout << "this" << endl;
                return false;
            }
            else
            {
                ++left;
                --right;
            }
        }
        return true;
    }
};