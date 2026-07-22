class Solution:
    def goodNodes(self, root):

        def dfs(node, maxVal):
            if not node:
                return 0

            good = 0
            if node.val >= maxVal:
                good = 1

            maxVal = max(maxVal, node.val)

            return good + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val)