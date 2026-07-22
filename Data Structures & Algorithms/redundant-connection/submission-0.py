class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])   # Path Compression
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return False

            if rank[px] > rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]