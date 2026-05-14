# Kth Smallest Integer in BST: https://neetcode.io/problems/kth-smallest-integer-in-bst/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _inOrderTrav(self, node: Optional[TreeNode], sortedList: list[int]) -> None:
        if not node:
            return

        self._inOrderTrav(node.left, sortedList)
        sortedList.append(node.val)
        self._inOrderTrav(node.right, sortedList)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedList = []
        self._inOrderTrav(root, sortedList)
        return sortedList[k-1]