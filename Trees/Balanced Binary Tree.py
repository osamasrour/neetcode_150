# Balanced Binary Tree: https://neetcode.io/problems/balanced-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        curr = root
        if not curr: return True

        left = self.trace(curr.left)
        right = self.trace(curr.right)
        if left < 0 or right < 0: return False
        return abs(left - right) <= 1

    def trace(self, node):
        if not node: return 0

        left = self.trace(node.left)
        right = self.trace(node.right)

        if left < 0 or right < 0 or not (abs(left - right) <= 1): return -1

        return max(left, right) + 1