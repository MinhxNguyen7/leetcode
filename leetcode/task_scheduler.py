from collections import Counter


# Reference: https://leetcode.com/problems/task-scheduler/solutions/699297/python-very-detailed-explanation-with-examples/
class Solution:
    @staticmethod
    def leastInterval(tasks: list[str], n: int) -> int:
        counter: Counter[str] = Counter(tasks)

        max_freq: int = counter.most_common(1)[0][1]

        return max(
            (max_freq - 1) * (n + 1) + list(counter.values()).count(max_freq),
            len(tasks)
        )

if __name__ == '__main__':
    print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
    # print(Solution().leastInterval(["A","A","A","B","B","B"], 0))