# Reverse Linked List: https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150

from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not head:
            return None
        if current.next == None:
            return head

        prev = current
        current = current.next
        _next = current.next
        prev.next = None
        while _next:
            current.next = prev
            prev = current
            current = _next
            _next = current.next
        current.next = prev
        return current
