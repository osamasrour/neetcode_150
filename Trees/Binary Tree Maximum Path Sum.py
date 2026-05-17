# Binary Tree Maximum Path Sum: https://neetcode.io/problems/binary-tree-maximum-path-sum/question

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrderTrav(self, root: Optional[TreeNode], lst: list[int]):
        if not root: return

        self.inOrderTrav(root.left, lst)
        lst.append(root.val)
        self.inOrderTrav(root.right, lst)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        inOrdLst: list[int] = []
        self.inOrderTrav(root, inOrdLst)
        print("inOrdLst = ", inOrdLst)
        maxSum = float("-inf")
        n = len(inOrdLst)
        for i in range(n):
            for j in range(n, i, -1):
                s = sum(inOrdLst[i: j])
                maxSum = max(s, maxSum)

        return maxSum
