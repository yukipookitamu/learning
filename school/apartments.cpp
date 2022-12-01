#include <iostream>
#include <vector>

using namespace std;

int main() {

    int applicants;
    int freeApts;
    int k;
    vector<int> desSize; // desired size
    vector<int> availSize;
    cin >> applicants;
    cin >> freeApts;
    cin >> k;
    int count = 0;

    for (int i = 0; i < applicants; i++) {
        int size;
        cin >> size;
        desSize.push_back(size);
    }

    for (int j = 0; j < freeApts; j++) {
        int size;
        cin >> size;
        availSize.push_back(size);
    }

    for (vector<int>::iterator s = desSize.begin(); s != desSize.end(); ++s) {
        for (vector<int>::iterator a =availSize.begin(); a != availSize.end(); ++a) {
            if((*a >= *s-k) || (*a <= *s+k)) {
                count++;
                availSize.erase(a);
            }
            // cout << *a << endl;
        }
    }

    cout << count;

    return 0;
}