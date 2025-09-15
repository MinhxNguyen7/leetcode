class Solution:
    @staticmethod
    def _h_delta(citations: list[int], index: int):
        """
        Difference between indexed paper's citations and the number
        of papers that have at least that many citations.
        """
        return citations[index] - (len(citations) - index)

    def hIndex(self, citations: list[int]) -> int:
        if len(citations) == 1:
            return 1 if citations[0] > 0 else 0

        if len(citations) == 2:
            return 0 if citations[1] == 0 else (2 if citations[0] >= 2 else 1)

        left = 0
        right = len(citations) - 1

        while left + 1 < right:
            mid = (right - left) // 2 + left

            h_delta = Solution._h_delta(citations, mid)

            print(f"Left: {left}, right: {right}, mid: {mid}, h_delta: {h_delta}")

            if h_delta == 0:
                return citations[mid]
            elif h_delta > 0:
                right = mid
            else:
                left = mid

        return max(
            min(citations[left], len(citations) - left),
            min(citations[right], len(citations) - right),
        )


if __name__ == "__main__":
    print(Solution().hIndex([0, 1, 2, 3, 6, 7, 8]))
    print(Solution().hIndex([3, 3, 3]))
