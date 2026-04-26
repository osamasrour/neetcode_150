# Merge K Sorted Linked Lists: https://neetcode.io/problems/merge-k-sorted-linked-lists/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        all_nodes = []
        for i in range(k):
            curr = lists[i]
            while curr:
                all_nodes.append(curr.val)
                curr = curr.next

        all_nodes.sort()
        dummy = ListNode(0)
        curr = dummy
        i = 0
        while len(all_nodes) > i:
            curr.next = ListNode(all_nodes[i])
            curr = curr.next
            i+=1
        curr.next = None
        return dummy.next