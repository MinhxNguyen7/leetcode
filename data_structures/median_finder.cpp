#include <queue>
#include <iostream>
#include <cmath>

class MedianFinder {
    // Max heap of numbers smaller than the median
    std::priority_queue<int, std::vector<int>, std::less<int>> subMedian;

    // Min heap of numbers greater than the median
    std::priority_queue<int, std::vector<int>, std::greater<int>> superMedian;

public:    
    void addNum(int num) {
        const double median = findMedian();

        if (num > median) {
            superMedian.push(num);
        } else {
            subMedian.push(num);
        }

        if (superMedian.size() >= subMedian.size() + 2) {
            subMedian.push(superMedian.top());
            superMedian.pop();
        } else if (subMedian.size() >= superMedian.size() + 2) {
            superMedian.push(subMedian.top());
            subMedian.pop();
        }
    }
    
    double findMedian() {
        if (subMedian.empty() && superMedian.empty()) {
            return NAN;
        } else if (subMedian.empty()) {
            return superMedian.top();
        } else if (superMedian.empty()) {
            return subMedian.top();
        }

        if (subMedian.size() == superMedian.size()) {
            return static_cast<double>(subMedian.top() + superMedian.top()) / 2;
        }

        if (superMedian.size() > subMedian.size()) {
            return superMedian.top();
        } else {
            return subMedian.top();
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */

int main() {
    MedianFinder medianFinder = MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    std::cout << medianFinder.findMedian() << "\n"; // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0
}