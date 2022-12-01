#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    
    int n; // number of vals
    unordered_set<int> s;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        s.insert(num);
    }

    cout << s.size();
    
    return 0;
}