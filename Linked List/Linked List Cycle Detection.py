# Linked List Cycle Detection: https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        hashLst = set()
        while current:
            if current not in hashLst and current != None:
                hashLst.add(current)
            else:
                return True
            current = current.next

        return False