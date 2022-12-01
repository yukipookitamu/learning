#include <bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        // if empty
        if (head == nullptr) {
            return head;
        }
        
        ListNode* curr = head;
        ListNode* next = curr->next;
        while (next) {
            // If same, stay at node just skip
            if (curr->val == next->val) {
                // if tail
                if (next->next == nullptr) {
                    curr->next = nullptr;
                    next = nullptr;
                }
                else {
                    curr->next = next->next;
                    next = next->next;
                }
            }
            else {
                curr = curr->next;
                next = curr->next;
            }
        }
        return head;
    }
};