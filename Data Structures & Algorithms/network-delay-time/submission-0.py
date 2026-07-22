import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        minHeap = [(0, k)]   # (time, node)
        dist = {}

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in dist:
                continue

            dist[node] = time

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(
                        minHeap,
                        (time + weight, nei)
                    )

        if len(dist) != n:
            return -1

        return max(dist.values())