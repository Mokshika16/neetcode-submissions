import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}

        queries_sorted = sorted(queries)

        heap = []  # (interval length, right end)
        i = 0

        for q in queries_sorted:
            # Add intervals that start before query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            # Remove expired intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Smallest valid interval
            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]