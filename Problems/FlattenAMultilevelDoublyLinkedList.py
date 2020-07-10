"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

from Node import Node


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        temp = head
        stack = []
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif head.next is None and stack:
                head.next = stack.pop()
                head.next.prev = head
            head = head.next
        return temp

if __name__ == "__main__":
    head = Node.Node(1, None, None, None)
    s = Solution()
    s.flatten(head)