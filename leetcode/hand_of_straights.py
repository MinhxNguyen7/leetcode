from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False

        hand.sort(reverse=True)
        counter = Counter(hand)

        while hand:
            bottom = hand[-1]
            count = counter[bottom]

            if count == 0:
                del counter[bottom]
                hand.pop()
            else:
                for value in range(bottom, bottom + groupSize):
                    if value not in counter or counter[value] < count:
                        return False
                    counter[value] -= count

        return True

