class Solution:
    @staticmethod
    def square(n: int):
        return n**2

    @staticmethod
    def process(n: int):
        digits = [int(d) for d in str(n)]

        return sum(map(__class__.square, digits))

    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            if n == 1:
                return True

            if n in seen:
                return False

            seen.add(n)
            n = __class__.process(n)


if __name__ == "__main__":
    print(Solution().isHappy(19))  # Expect True
    print(Solution().isHappy(2))  # Expect False
