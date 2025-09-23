class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = list(dominoes)

        last_r = last_l = -1

        for i, c in enumerate(dominoes):
            match c:
                case "L":
                    # If this is the first fallen domino or the last one was
                    # also falling left.
                    if last_r == -1 or last_l > last_r:
                        for j in range(max(last_l, 0), i):
                            res[j] = "L"
                    else:  # Last one was falling right
                        # Mark "R" and "L" from the two sides until pointers meet
                        l_marker = i
                        r_marker = last_r

                        while l_marker > r_marker:
                            res[l_marker] = "L"
                            res[r_marker] = "R"

                            l_marker -= 1
                            r_marker += 1

                    last_l = i
                case "R":
                    # If the last fallen one was also falling right,
                    # all the dominoes in between should fall right as well
                    if last_r > last_l:
                        for j in range(last_r, i):
                            res[j] = "R"

                    last_r = i
                case ".":
                    pass

        # If the last fallen one was falling right, mark the rest of them right
        if last_r > last_l:
            for j in range(last_r, len(dominoes)):
                res[j] = "R"

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.pushDominoes(".L.R...LR..L.."))  # "LL.RR.LLRRLL.."
