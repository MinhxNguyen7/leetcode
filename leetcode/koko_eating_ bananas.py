from functools import reduce

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        total = sum(piles)

        left = (total + 1) // h
        right = max(size for size in piles)

        speed: int = 0
        last_valid = right

        while left <= right:
            speed = (left + right) // 2
            
            if speed == 0: break

            time_taken = reduce(
                int.__add__, 
                ((pile / speed).__ceil__() for pile in piles)
            )

            if time_taken > h: # Cannot finish in time
                left = speed + 1
            else:
                last_valid = speed
                right = speed - 1

        return last_valid
    
if __name__ == '__main__':
    print(Solution().minEatingSpeed([312884470], 968709470))
    print(Solution().minEatingSpeed([3,6,7,11], 8))
    print(Solution().minEatingSpeed([30,11,23,4,20], 5))