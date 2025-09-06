#include <bits/stdc++.h>

// Returns a map of revenue rate to amount of bandwidth delivarable at that revenue
std::map<double, size_t, std::greater<double>> extractRevenueRates(
    const std::vector<int>& sizes, const std::vector<int>& revenues
) {
    std::map<double, size_t, std::greater<double>> rates{};

    auto sizeIt{sizes.begin()}, revIt{revenues.begin()};
    for (; 
        sizeIt < sizes.end() && revIt < revenues.end(); 
        ++sizeIt, ++revIt
    ) {
        const auto size{*sizeIt}, rev{*revIt};
        const double revRate{(double) rev / size};
        
        const auto rateIt = rates.find(revRate);
        if (rateIt != rates.end()) {
            rateIt->second += size;
        } else {
            rates.insert({revRate, size});
        }
    }

    return rates;
}


double allocateBandwidthMaxRevenue(
    int N, std::vector<int> sizes, std::vector<int> revenues, long B
) {
    (void)N;

    const auto rates{extractRevenueRates(sizes, revenues)};

    double accumulatedRevenue{};
    size_t remainingBandwidth{static_cast<size_t>(B)};

    for (auto [rate, size] : rates) {
        if (size > remainingBandwidth) {
            return accumulatedRevenue + rate * remainingBandwidth;
        }

        accumulatedRevenue += rate * size;
        remainingBandwidth -= size;
    }

    return accumulatedRevenue;
}


int main() {
    std::cout << allocateBandwidthMaxRevenue(3, {10, 20, 30}, {60, 100, 120}, 50) << '\n';
    std::cout << allocateBandwidthMaxRevenue(4, {1, 2, 3, 4}, {10, 20, 30, 40}, 10) << '\n';
}