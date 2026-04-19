# Copy Linked List with Random Pointer: https://neetcode.io/problems/copy-linked-list-with-random-pointer/question?list=neetcode150

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return None

        copyMap = dict()
        current = head
        while current:
            copyMap[current] = Node(current.val)
            current = current.next

        for real, copy in copyMap.items():
            if real.next: copy.next = copyMap[real.next]
            if real.random: copy.random = copyMap[real.random]

        return copyMap[head]