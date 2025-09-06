class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:
    Node* connect(Node* root) {
       auto next_start{root};

       while (next_start) {
        // Populate next level by traversing current one
        auto current{next_start};
        while (current and current->left and current->right) {
            current->left->next = current->right;
            current->right->next = current->next ? current->next->left : nullptr;
            current = current->next; 
        }

        // Switch to next level
        next_start = next_start->left;
       }

       return root;
    }
};
