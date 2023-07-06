#include <unordered_map>
#include <iostream>

struct DequeNode {
    int key;
    int value;
    DequeNode* prev;
    DequeNode* next;
    DequeNode(int key, int value, DequeNode* prev = nullptr, DequeNode* next = nullptr):
        key{key}, value{value}, prev{prev}, next{next} {};
};

class LRUCache {
private:
    unsigned capacity;
    std::unordered_map<int, DequeNode*> map;
    DequeNode* const head;
    DequeNode* const tail;

    DequeNode* getNode(const int key) {
        auto keyIt{map.find(key)};

        if (keyIt == map.end()) return nullptr;

        // Key exists
        DequeNode* node{keyIt->second};

        // Remove from queue
        DequeNode* prev{node->prev};
        DequeNode* next{node->next};
        next->prev = prev;
        prev->next = next;

        // Place at the start 
        next = head->next;
        head->next = node;
        node->prev = head;
        node->next = next;
        next->prev = node;

        return node;
    }

public:
    LRUCache(int capacity): 
        capacity{static_cast<unsigned>(capacity)}, 
        head{new DequeNode(0, 0)},
        tail{new DequeNode(0, 0)}
    {
        tail->prev = head;
        head->next = tail;
    }
    
    int get(int key) {
        DequeNode* const node{getNode(key)};

        if (!node) return -1;
        return node->value;
    }
    
    void put(int key, int value) {
        // Gets pointer to node and places the node at the start of the queue
        DequeNode* node{getNode(key)};

        // Just change the value if the node already exists
        if (node) {
            node-> value = value;
            return;
        }

        // Add node to start of queue
        DequeNode* next{head->next};
        node = new DequeNode(key, value, head, next);
        next->prev = node;
        head->next = node;

        // Add node to mapping
        map.insert_or_assign(key, node);


        // If capacity is exceeded
        if (map.size() > capacity) {
            DequeNode* const toDelete{tail->prev};
            const int deleteKey{toDelete->key};

            // Remove from the end of queue
            DequeNode* prev{toDelete->prev};
            prev->next = tail;
            tail->prev = prev;
            delete toDelete;

            // Remove from mapping
            map.erase(deleteKey);
        }
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

int main() {
    LRUCache cache{2};

    cache.put(1, 1);
    std::cout << cache.get(1) << '\n';
    cache.put(2, 2);
    cache.put(3, 3);
    std::cout << cache.get(1) << '\n';
    std::cout << cache.get(2) << '\n';
    std::cout << cache.get(3) << '\n';

}