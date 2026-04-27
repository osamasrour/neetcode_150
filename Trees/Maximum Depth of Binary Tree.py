# Maximum Depth of Binary Tree: https://neetcode.io/problems/depth-of-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        if not curr:
            return 0
        return max(self.maxDepth(curr.left), self.maxDepth(curr.right)) + 1