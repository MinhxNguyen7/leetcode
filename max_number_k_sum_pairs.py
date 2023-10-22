from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        counter = Counter(num for num in nums if num < k)

        ret = 0
        for num, count in counter.items():
            other = k - num
            if other < num: continue # Don't double count
            if other == num:
                ret += count // 2
            else:
                ret += min(counter.get(other, 0), count)

        return ret
    
if __name__ == '__main__':
    # Expect 2
    print(Solution().maxOperations([1,2,3,4], 5))
