import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x * x + y * y
            heap.append((dist, x, y))

        heapq.heapify(heap)

        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res   