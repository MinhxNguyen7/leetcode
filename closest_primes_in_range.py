from math import ceil, sqrt

class Solution:
    @staticmethod
    def get_primes(left: int, right: int) -> list[int]:
        composite = [False] * (right + 1)

        composite[0] = composite[1] = True

        for num in range(ceil(sqrt(right)) + 1):
            if composite[num]: continue

            for multiple in range(num * 2, right + 1, num):
                composite[multiple] = True

        return [num for num in range(left, right + 1) if not composite[num]]

    @staticmethod
    def closestPrimes(left: int, right: int) -> list[int]:
        if right < 3: return [-1, -1]

        primes = Solution.get_primes(left, right)
        if len(primes) < 2: return [-1, -1]
            
        pair = [primes[0], primes[1]]
        min_dist = primes[1] - primes[0]

        for index in range(len(primes) - 1):
            dist = primes[index + 1] - primes[index]
            if dist < min_dist:
                min_dist = dist
                pair = [primes[index], primes[index + 1]]

        return pair
    
if __name__ == '__main__':
    print(Solution().closestPrimes(10, 19))