#
# Complete the 'longestAlternatingSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

from typing import Literal


zero_one_t = Literal["0", "1"]


def calculate_expected(index: int, start: zero_one_t) -> zero_one_t:
    if not index % 2:
        return start

    return "1" if start == "0" else "0"


def max_length_with_start(s: str, k: int, start: zero_one_t):
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] != calculate_expected(right, start):
            k -= 1

        # Shrink substring until a wrong character encountered to recover flip
        while k < 0:
            if s[left] != calculate_expected(left, start):
                k += 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def longestAlternatingSubstring(s: str, k: int):
    return max(max_length_with_start(s, k, "0"), max_length_with_start(s, k, "1"))


if __name__ == "__main__":
    print(longestAlternatingSubstring("010101", 0))  # 6
