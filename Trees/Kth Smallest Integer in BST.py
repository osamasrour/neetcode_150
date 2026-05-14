# Kth Smallest Integer in BST: https://neetcode.io/problems/kth-smallest-integer-in-bst/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _inOrderTrav(self, node: Optional[TreeNode], sortedList: list[int], k: int) -> None:
        if not node:
            return

        self._inOrderTrav(node.left, sortedList, k)
        if len(sortedList) == k: return None
        sortedList.append(node.val)
        self._inOrderTrav(node.right, sortedList, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedList = []
        self._inOrderTrav(root, sortedList, k)
        return sortedList[-1]