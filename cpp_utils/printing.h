#include <vector>
#include <iostream>

template <typename Iterator>
void printIt(Iterator begin, Iterator end) {
    std::cout << '[';

    if (begin == end) {
        std::cout << ']';
        return;
    }

    std::cout << *(begin++);
    
    for (; begin != end; ++begin) {
        std::cout << ", " << *begin;
    }

    std::cout << ']';
}
