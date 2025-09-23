from heapq import heapify, heappush, heappop
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        res: list[str] = []

        heap: list[tuple[int, str]] = [
            (-count, char) for char, count in Counter(s).items()
        ]
        heapify(heap)

        while heap:
            first_count, first_char = heappop(heap)
            first_count *= -1

            if not heap:
                # If only one character remains with multiple count
                # or the last-chosen character is the same
                if first_count > 1 or (res and res[-1] == first_char):
                    return ""

                res.append(first_char)
                break

            second_count, second_char = heappop(heap)
            second_count *= -1

            if (not res) or res[-1] != first_char:
                # Lead with first_char
                res.append(first_char)
                res.append(second_char)
            else:
                # Lead with second_char
                res.append(second_char)
                res.append(first_char)

            first_count -= 1
            second_count -= 1

            if first_count:
                heappush(heap, (-first_count, first_char))

            if second_count:
                heappush(heap, (-second_count, second_char))

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()

    print(sol.reorganizeString("aab"))  # "aab"
