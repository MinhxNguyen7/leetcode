class Solution:
    @staticmethod
    def removeDuplicates(nums: list[int]) -> int:
        current = -101
        k = 0

        for i, num in enumerate(nums):
            if num != current:
                current = num
                k += 1
            else:
                nums[i] = 101

        left = right = 0
        while True:
            # Find first gap
            while nums[left] != 101:
                left += 1
                if left == len(nums):
                    return k

            # Find first subsequent number
            right = max(left, right)
            while nums[right] == 101:
                right += 1
                if right == len(nums):
                    return k

            nums[left] = nums[right]
            nums[right] = 101


if __name__ == '__main__':
    l1 = [1,1,2]
    print(Solution.removeDuplicates(l1)) # 2
    print(l1) # [1, 2, _]
    
    l2 = [0,0,1,1,1,2,2,3,3,4]
    print(Solution.removeDuplicates(l2)) # 5
    print(l2) # [0,1,2,3,4,_,_,_,_,_]
