# Merge K Sorted Linked Lists: https://neetcode.io/problems/merge-k-sorted-linked-lists/question?list=neetcode150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def lstToLlst(lst: list) -> Optional[ListNode]:
    if lst == []: return None
    head = ListNode(lst[0])
    curr = head
    i = 1
    while i < len(lst):
        curr.next = ListNode(lst[i])
        i+=1
        curr = curr.next

    return head

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        sortedListK = []
        listk = []
        while True:
            
            for i in range(k):
                node = lists[i]
                if not node or node in listk: continue
                listk.append(node)
                
                lists[i] = lists[i].next
            if not listk: break

            listk.sort(key=lambda x: x.val,reverse=True)
            print([i.val for i in listk])
            sortedListK.append(listk.pop().val)
        # print(sortedListK)
        poped = ListNode(sortedListK.pop()) if sortedListK else None

        while sortedListK:
            node = ListNode(sortedListK.pop())
            node.next = poped
            poped = node

        return poped




lists = [lstToLlst([1,2,4]),lstToLlst([1,3,5]),lstToLlst([3,6])]
print(Solution().mergeKLists(lists).val)