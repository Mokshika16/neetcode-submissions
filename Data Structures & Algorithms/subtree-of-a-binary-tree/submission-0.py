class Solution:
    def isSubtree(self, root, subRoot):

        def isSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return (isSame(p.left, q.left) and
                    isSame(p.right, q.right))

        if not root:
            return False

        if isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
                