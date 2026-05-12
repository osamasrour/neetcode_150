# Count Good Nodes in Binary Tree: https://neetcode.io/problems/count-good-nodes-in-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        hMap: set[int] = set()
        stack = []
        self._goodNodes(root, hMap, stack)
        return len(hMap)

    def _goodNodes(self, node: TreeNode, HashMap: set[int], stack: list) -> bool:
        add = False
        if not node:
            for e in stack:
                HashMap.add(e)
            return add

        if stack:
            if node.val > stack[-1]:
                stack.append(node.val)
                add = True
        else:
            stack.append(node.val)
            add = True

        print(stack)
        l_add = self._goodNodes(node.left, HashMap, stack)
        if l_add: stack.pop()
        r_add = self._goodNodes(node.right, HashMap, stack)
        if r_add: stack.pop()
        return add