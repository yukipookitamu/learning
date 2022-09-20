#include <bits/stdc++.h>

class Solution
{
public:
    bool isPalindrome(string s)
    {
        // convert string to back to lower case
        std::for_each(s.begin(), s.end(), [](char &c)
                      { c = ::tolower(c); });
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