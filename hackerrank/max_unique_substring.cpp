#include <algorithm>
#include <string>
#include <iostream>
#include <bitset>

/*
 * Complete the 'maxDistinctSubstringLengthInSessions' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING sessionString as parameter.
 */

int maxDistinctSubstringLengthInSessions(const std::string& sessionString) {
    unsigned max_len{};
    std::bitset<26> bag{};
    
    auto left{sessionString.begin()};
    for (
        auto right{sessionString.begin()}; 
        right < sessionString.end(); 
        ++right
    ) {
        const auto c{*right};
        
        if (c == '*') {
            bag.reset();
            left = right + 1;
        } else {
            const int charIdx{c - 'a'};
            
            while(bag[charIdx]) {
                bag.reset(*left - 'a');
                ++left;
            }
            
            bag.set(charIdx);
            
            const unsigned length = right - left + 1;
            max_len = std::max(length, max_len);
        }
    }
    
    return max_len;
}

int main() {
    std::cout << maxDistinctSubstringLengthInSessions("*") << '\n'; // 0
    std::cout << maxDistinctSubstringLengthInSessions("abcabcbb") << '\n'; // 3
}