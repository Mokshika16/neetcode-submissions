class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        oldToCopy = {}

        curr = head

        # Create copy of each node
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # Assign next and random pointers
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy.get(curr.next)
            copy.random = oldToCopy.get(curr.random)
            curr = curr.next

        return oldToCopy[head]