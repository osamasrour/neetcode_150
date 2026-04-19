# Remove Node From End of Linked List: https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 0
        current = head
        while current:
            s+=1
            current = current.next

        rm_idx = s - n
        i = 0
        current = head
        while current:
            if i == rm_idx:
                if i == 0:
                    head = head.next
                    return head
                else:
                    prev.next = current.next
                    current.next = None
                    return head

            prev = current
            current = current.next
            i+=1

        return head