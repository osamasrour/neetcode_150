# Invert Binary Tree: https://neetcode.io/problems/invert-a-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        if not root:
            return None
        if curr.left: 
            self.invertTree(curr.left)
            curr.left, curr.right = curr.right, curr.left

        return curr