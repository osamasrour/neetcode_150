# Add Two Numbers: https://neetcode.io/problems/add-two-numbers/question?list=neetcode150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reversedNum(self, head: Optional[ListNode]) -> int:
        curr = head
        units = []
        while curr:
            units.append(curr.val)
            curr = curr.next

        units.reverse()
        num = 0
        i = 0
        while i < len(units):
            num = (num * 10) + units[i]
            i+=1
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.reversedNum(l1)
        num2 = self.reversedNum(l2)
        total = num1 + num2
        if total == 0:
            return ListNode(0)
        units = []
        while total:
            ones = total % 10
            units.append(ones)
            total = (total - ones) // 10

        new_head = ListNode(units[0])
        curr = new_head
        i = 1
        while i < len(units):
            curr.next = ListNode(units[i])
            curr = curr.next
            i+=1
        curr.next = None
        return new_head