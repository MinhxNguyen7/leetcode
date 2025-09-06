class Solution:
    @staticmethod
    def say(digits: str) -> str:
        words: list[int] = []

        current = digits[0]
        count = 0
        for digit in digits:
            if current != digit:
                words.append(count)
                words.append(int(current))
                
                current = digit
                count = 0

            count += 1

        words.append(count)
        words.append(int(digit))
        
        return "".join(map(str, words))

    @staticmethod
    def countAndSay(n: int) -> str:
        if n == 1: return "1"

        return Solution.say(Solution.countAndSay(n-1))
    
    
if __name__ == '__main__':
    print(Solution.countAndSay(1))  # 1
    print(Solution.countAndSay(2))  # 11
    print(Solution.countAndSay(3))  # 21
    print(Solution.countAndSay(4))  # 1211

    
    