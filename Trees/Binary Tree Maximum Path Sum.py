# Binary Tree Maximum Path Sum: https://neetcode.io/problems/binary-tree-maximum-path-sum/question

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], maxPath: list[int]):
        if not node: return 0

        leftPath  = self.dfs(node.left , maxPath)
        rightPath = self.dfs(node.right, maxPath)
        termVal = node.val + leftPath + rightPath
        val = max(node.val, node.val + leftPath, node.val + rightPath)
        maxPath[0] = max(maxPath[0], termVal, val)
        return val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]
        self.dfs(root, res)
        return res[0]