#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    template<typename Iterator>
    static ListNode* createList(Iterator begin, Iterator end);

    void print();
};

// Templated function to create a singly-linked list from begin and end iterators
template<typename Iterator>
ListNode* ListNode::createList(Iterator begin, Iterator end) {
    if (begin == end) {
        return nullptr;
    }
    
    ListNode* head = new ListNode(*begin);
    ListNode* current = head;
    ++begin;
    
    while (begin != end) {
        current->next = new ListNode(*begin);
        current = current->next;
        ++begin;
    }
    
    return head;
}

// Function to print the linked list
void ListNode::print() {
    ListNode* current = this;
    while (current != nullptr) {
        std::cout << current->val;
        if (current->next != nullptr) {
            std::cout << " -> ";
        }
        current = current->next;
    }
    std::cout << std::endl;
}

