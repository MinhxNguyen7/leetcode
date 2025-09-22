#include "data_structures/linkedList.h"
#include <vector>

class Solution
{
    static unsigned computeGcd(unsigned a, unsigned b)
    {
        while (b != 0)
        {
            const unsigned tmp{b};
            b = a % b;
            a = tmp;
        }

        return a;
    }

public:
    static ListNode *insertGreatestCommonDivisors(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }

        ListNode *curr{head};
        for (
            ListNode *next{curr->next};
            next != nullptr; curr = next,
                             next = next->next)
        {
            unsigned gcd = computeGcd(
                static_cast<unsigned>(curr->val),
                static_cast<unsigned>(next->val));

            ListNode *newNode = new ListNode(gcd, next);
            curr->next = newNode;
        }

        return head;
    }
};

int main()
{
    std::vector<int> listVals{18, 6, 10, 3};
    auto list = ListNode::createList(listVals.begin(), listVals.end());
    list = Solution::insertGreatestCommonDivisors(list);
    list->print();
}