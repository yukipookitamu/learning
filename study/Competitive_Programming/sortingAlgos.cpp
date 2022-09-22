#include <bits/stdc++.h>

// Competitive Programmer's Handbook Chapter 3: Sorting

using namespace std;

class Sorting
{
public:
    void bubbleSort(vector<int> nums)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            for (int j = 0; j < nums.size(); j++)
            {
                if (nums[j] > nums[j + 1])
                {
                    swap(nums[j], nums[j + 1]);
                }
            }
        }
    }
};

int main()
{
    Sorting sort;

    vector<int> numbers{1, 3, 9, 2, 7, 3};
    for (int x : numbers)
    {
        cout << x << " ";
    }
    cout << endl;

    sort.bubbleSort(numbers);

    for (int x : numbers)
    {
        cout << x << " ";
    }

    return 0;
}