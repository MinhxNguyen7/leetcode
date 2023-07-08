#include <queue>
#include <iostream>

class Solution {
private: 
    void appendToQueue(TreeNode* root, std::priority_queue<int>& queue, int max_size) {
        if (root == nullptr) return;

        queue.push(root->val);
        if (queue.size() > max_size) queue.pop();
        appendToQueue(root->left, queue, max_size);
        appendToQueue(root->right, queue, max_size);
    }

public:
    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int> queue{};

        appendToQueue(root, queue, k);

        return queue.top();
    }
};