from itertools import chain, repeat
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(
            chain(*(repeat(char, count) for char, count in Counter(s).most_common()))
        )


if __name__ == "__main__":
    sol = Solution()

    print(sol.frequencySort("tree"))  # "eert"
    print(sol.frequencySort("cccaaa"))  # "aaaccc"
