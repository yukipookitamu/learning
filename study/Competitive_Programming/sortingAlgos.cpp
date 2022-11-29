#include <bits/stdc++.h>

// Competitive Programmer's Handbook Chapter 3: Sorting

using namespace std;

class Sorting
{
public:
    vector<int> bubbleSort(vector<int> nums)
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
        return nums;
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

    numbers = sort.bubbleSort(numbers);

    for (int x : numbers)
    {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}