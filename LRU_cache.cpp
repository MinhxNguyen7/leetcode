#include <iostream>
#include <unordered_map>

struct Node {
    const int key;
    int value;
    Node* prev;
    Node* next;
};

class LRUCache {
private:
    const unsigned capacity;

    Node* head;
    Node* tail;
    
    std::unordered_map<int, Node*> keyToNode;

    bool conditionallyEvict() {
        if (keyToNode.size() > capacity) {
            Node* oldTail = tail;
            tail = tail->prev;

            keyToNode.erase(oldTail->key);
            delete oldTail;
            return true;
        }

        return false;
    }

    // Moves the node to the front of the list.
    // Assumes that the key exists.
    void markAccessed(int key) {
        auto node = keyToNode.find(key)->second;
        
        if (node == head) {
            return;
        }

        if (node == tail) {
            tail = tail->prev;
            tail->next = nullptr;
        } else {
            node->prev->next = node->next;
            node->next->prev = node->prev;
        }

        insertAtHead(node);
    }

    void insertAtHead(Node* node) {
        node->next = head;
        if (head) {
            head->prev = node;
            head = node;
        } else {
            head = tail = node;
        }
    }

public:
    LRUCache(int capacity): 
        capacity{static_cast<unsigned>(capacity)}, 
        head{}, tail{}, keyToNode{}
    {}
    
    int get(int key) {
        auto iterator = keyToNode.find(key);
        
        if (iterator == keyToNode.end()) {
            return -1;
        }

        markAccessed(key);
        return iterator->second->value;
    }
    
    void put(int key, int value) {
        auto iterator = keyToNode.find(key);
        
        if (iterator == keyToNode.end()) {
            Node* newNode = new Node{key, value, nullptr, head};
            
            insertAtHead(newNode);
            keyToNode.emplace(key, newNode);
            
            conditionallyEvict();
        } else {
            iterator->second->value = value;
            markAccessed(key);
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
    auto cache = LRUCache(3);

    cache.put(1, 1);
    cache.put(2, 2);
    cache.put(3, 3);
    cache.put(4, 4); // Evicts key 1
    std::cout << cache.get(4) << "\n"; // Returns 4
    std::cout << cache.get(3) << "\n"; // Returns 3
    std::cout << cache.get(2) << "\n"; // Returns 2
    std::cout << cache.get(1) << "\n"; // Returns -1 (not found)
    cache.put(5, 5); // Evicts key 4
    std::cout << cache.get(1) << "\n"; // Returns -1 (not found)
    std::cout << cache.get(2) << "\n"; // Returns 2
    std::cout << cache.get(3) << "\n"; // Returns 3
    std::cout << cache.get(4) << "\n"; // Returns -1 (not found)
    std::cout << cache.get(5) << "\n"; // Returns 5
}