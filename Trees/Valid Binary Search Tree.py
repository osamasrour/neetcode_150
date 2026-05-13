# Valid Binary Search Tree: https://neetcode.io/problems/valid-binary-search-tree/question?list=neetcode150

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


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        sortedList = []

        self._inOrderTrav(root, sortedList)
        n = len(sortedList)
        for i in range(n - 1):
            if sortedList[i] >= sortedList[i+1]:
                return False

        return True

