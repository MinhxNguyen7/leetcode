#include <iostream>
#include <vector>

#include "data_structures/linkedList.h"


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == nullptr) return nullptr;

        ListNode** inPtrPtr{&head}; // Pointer to the next pointer of the prev node
        
        while (*inPtrPtr != nullptr) {
            ListNode* first{*inPtrPtr};
            ListNode* const second = first->next;
            
            if (second == nullptr) break;

            *inPtrPtr = second;
            first->next = second->next;
            second->next = first;
            
            inPtrPtr = &first->next;
        }

        return head;
    }
};


int main() {
    std::vector<int> values = {1, 2, 3, 4};
    ListNode* head = ListNode::createList(values.begin(), values.end());

    head = Solution().swapPairs(head);
    head->print();

    return 0;
}
