import heapq

class Solution:
    def minCostConnectPoints(self, points):

        n = len(points)
        adj = [[] for _ in range(n)]

        # Build graph
        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visit = set()

        minHeap = [(0, 0)]  # cost, point

        while len(visit) < n:

            cost, point = heapq.heappop(minHeap)

            if point in visit:
                continue

            visit.add(point)
            res += cost

            for neiCost, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(
                        minHeap,
                        (neiCost, nei)
                    )

        return res