# Linked List Cycle Detection: https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head

        lst: list[int] = []
        
        while True:
            if current not in lst and current != None:
                lst.append(current)

            elif current == None:
                return False

            else:
                return True
            current = current.next

        return False