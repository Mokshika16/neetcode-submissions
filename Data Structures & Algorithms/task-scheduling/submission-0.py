from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)

        # Max heap (negative frequencies)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()   # (remainingFreq, availableTime)

        while maxHeap or q:
            time += 1

            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)

                if freq:
                    q.append((freq, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time   