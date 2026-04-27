# Reverse Nodes in K-Group: https://neetcode.io/problems/reverse-nodes-in-k-group/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        headLst: list[ListNode] = []
        while curr:
            headLst.append(curr)
            curr = curr.next

        begging = 0
        end = k
        reversedK = []
        while begging < len(headLst):
            if end > len(headLst):
                reversedK.extend(headLst[begging: end])
                break
            else:
                reversedK.extend(reversed(headLst[begging: end]))
                begging = end
                end = end + k

        for i in range(len(reversedK) - 1):
            reversedK[i].next = reversedK[i+1]

        reversedK[-1].next = None

        return reversedK[0]