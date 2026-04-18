# Reorder Linked List: https://neetcode.io/problems/reorder-linked-list/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import ceil
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        current = head
        lst = []
        while current:
            n+=1
            lst.append(current)
            current = current.next

        new_head = head
        current = new_head

        i = 1
        flip = True
        odd = n % 2 == 1
        while (i <= ceil(n/2) and not odd) or (i < ceil(n/2) and odd):
            print(i, flip)
            if flip:
                current.next = lst[n - i]
                flip = False
            else:
                current.next = lst[i]
                i+=1
                flip = True
            current = current.next

        current.next = None
        head = new_head