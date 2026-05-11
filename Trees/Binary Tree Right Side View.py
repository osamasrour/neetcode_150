# Binary Tree Right Side View: https://neetcode.io/problems/binary-tree-right-side-view/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        array = []
        self._levelOrder(root, -1, array)
        return array

    def _levelOrder(self, root, level = -1, arr: list[list[int]]=[]) -> None:
        if not root: return None
        n = len(arr)
        level+=1
        if n <= level:
            arr.append([])
        arr[level].append(root.val)
        self._levelOrder(root.left, level, arr)
        self._levelOrder(root.right, level, arr)

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        levelsArray = self.levelOrder(root)
        result = []
        if not levelsArray: return []

        for i in levelsArray:
            result.append(i.pop())

        return result