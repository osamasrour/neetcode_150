# Count Good Nodes in Binary Tree: https://neetcode.io/problems/count-good-nodes-in-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count: list[int] = [0] # This is a hack, because we can't pass int by reference in Python.
        stack = []
        self._goodNodes(root, count, stack)
        return count[0]

    def _goodNodes(self, node: TreeNode, count: list[int], stack: list) -> bool:
        add = False
        if not node: return add

        if stack:
            if node.val >= stack[-1]:
                stack.append(node.val)
                count[0]+=1
                add = True
        else:
            stack.append(node.val)
            count[0]+=1
            add = True

        l_add = self._goodNodes(node.left, count, stack)
        if l_add: 
            stack.pop()
        r_add = self._goodNodes(node.right, count, stack)
        if r_add: 
            stack.pop()
        return add