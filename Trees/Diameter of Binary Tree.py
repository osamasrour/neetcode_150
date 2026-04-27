# Diameter of Binary Tree: https://neetcode.io/problems/binary-tree-diameter/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        return self.trace(root.left) + self.trace(root.right)

    def trace(self, root):
        if not root:
            return 0

        return max(self.trace(root.left), self.trace(root.right)) + 1



#     1
#         2
#     3        4
# 5