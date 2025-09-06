class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for index, char in enumerate(s):
            match char:
                case '(':
                    stack.append(index)
                case ')':
                    if not stack:
                        if not stars: return False
                        stars.pop()
                    else:
                        stack.pop()
                case '*':
                    stars.append(index)

        while stack:
            if not stars: return False
            if stack.pop() > stars.pop(): return False
        
        return True
    
if __name__ == '__main__':
    # Expect True
    print(Solution().checkValidString("()"))
    # Expect True
    print(Solution().checkValidString("(*)"))
    # Expect True
    print(Solution().checkValidString("(*))"))