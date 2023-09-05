class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        current = [0, 0, 0]
        
        for first, second, third in triplets:
            if (
                (first == target[0] and second <= target[1] and third <= target[2]) or
                (second == target[1] and first <= target[0] and third <= target[2]) or
                (third == target[2] and first <= target[0] and second <= target[1])
            ): current = [max(current[0], first), max(current[1], second), max(current[2], third)]
        
        return current == target

if __name__ == '__main__':
    print(Solution().mergeTriplets(
        [[3,5,1],[10,5,7]],
        [3,5,7]
    ))