# Merge Two Sorted Linked Lists: https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        new: Optional[ListNode]

        node1 = list1
        node2 = list2
        if node1.val <= node2.val:
            new = node1
            node1 = node1.next
        else:
            new = node2
            node2 = node2.next

        current = new
        while node1 and node2:

            if node1.val <= node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next

            current = current.next

        rest = node1 if node1 else node2

        while rest:
            current.next = rest
            rest = rest.next
            current = current.next

        current.next = None

        return new