from itertools import chain
from collections.abc import Iterable


class Solution:
    @staticmethod
    def _validate_section(s: str, start: int, end: int) -> bool:
        length = end - start
        return (
            (length != 0 and length <= 3)
            and (length == 1 or s[start] != "0")
            and int(s[start:end]) <= 255
        )

    @staticmethod
    def _make_ips(s: str, start: int, sections: int) -> Iterable[str]:
        assert sections >= 0 and sections <= 4

        if len(s) - start < sections or len(s) - start > sections * 3:
            return

        if sections == 0:
            yield ""
            return

        for sec_len in (1, 2, 3):
            end = start + sec_len
            if not Solution._validate_section(s, start, end):
                continue

            for following in Solution._make_ips(s, end, sections - 1):
                yield s[start:end] + (("." + following) if following else "")

    def restoreIpAddresses(self, s: str) -> list[str]:
        return list(Solution._make_ips(s, 0, 4))


if __name__ == "__main__":
    # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    print(Solution().restoreIpAddresses("25525511135"))

    # ["0.0.0.0"]
    print(Solution().restoreIpAddresses("0000"))

    # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    print(Solution().restoreIpAddresses("101023"))
