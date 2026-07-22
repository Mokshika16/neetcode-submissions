from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0]

            for i in range(start, start + groupSize):
                if count[i] == 0:
                    return False

                count[i] -= 1

                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True    