#include <iostream>
#include <unordered_set>

using namespace std;

int main()
{
    unordered_set<int> uset = {4, 1, 2, 3, 4, 2, 3};

    auto search = uset.find(2);
}