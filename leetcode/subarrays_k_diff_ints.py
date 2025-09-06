from collections import defaultdict

from tester import run_tests


class MyCounter(defaultdict[int, int]):
    def __init__(self):
        super().__init__(int)

    def increment(self, num: int):
        self[num] += 1

    def decrement(self, num: int):
        if self[num] == 1:
            del self[num]
            return
        
        self[num] -= 1
        

class Solution:
    """
    Reference: https://leetcode.com/problems/subarrays-with-k-different-integers/solutions/4945306/counting-subarrays-with-exactly-k-distinct-integers-a-sliding-window-adventure
    """
    
    @staticmethod
    def _sliding_window(nums: list[int], k: int) -> int:
        counter: MyCounter = MyCounter()
        good = 0

        left = 0
        for right, right_num in enumerate(nums):
            counter.increment(right_num)            

            while len(counter) > k:
                counter.decrement(nums[left])
                left += 1
                
            good += right - left + 1
            
        return good
    
    @staticmethod
    def subarraysWithKDistinct(nums: list[int], k: int) -> int:
        return Solution._sliding_window(nums, k) \
             - Solution._sliding_window(nums, k-1)
             

if __name__ == '__main__':
    run_tests(
        [7, 3],
        Solution.subarraysWithKDistinct,
        [
            ([1,2,1,2,3], 2),
            ([1,2,1,3,4], 3)
        ]
    )