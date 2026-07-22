from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            rightSide = None

            for _ in range(len(q)):
                node = q.popleft()
                rightSide = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(rightSide.val)

        return res