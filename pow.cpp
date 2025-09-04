#include <bitset>
#include <array>
#include <iostream>
#include <cmath>

class Solution {
    double powUnsigned(double x, unsigned n) {
        constexpr unsigned NUM_BITS{sizeof(int)*8};
        
        // 1-indexed array of x^(2^i)
        std::array<double, NUM_BITS> twoPowers;
        twoPowers[0] = x;
        for (unsigned i{1}; i < twoPowers.size(); ++i) {
            twoPowers[i] = twoPowers[i - 1] * twoPowers[i - 1];
        }
        
        double res{1};
        std::bitset<NUM_BITS> bitset{n};
        for (unsigned i{}; i < NUM_BITS; ++i) {
            if (bitset[i]) {
                res *= twoPowers[i];
            }
        }

        return res;
    }

public:
    double myPow(double x, int n) {
        if (n == 0) return 1;

        const double positivePowerResult{
            powUnsigned(x, static_cast<unsigned>(std::abs((long long) n)))
        };

        if (n > 0) {
            return positivePowerResult;
        }

        return 1.0 / positivePowerResult;
    }
};

int main() {
    Solution sol;

    std::cout << sol.myPow(2, 10) << '\n'; // 1024
    std::cout << sol.myPow(2, -2) << '\n'; // 0.25
}