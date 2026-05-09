# Subtree of Another Tree: https://neetcode.io/problems/subtree-of-a-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # TODO get rid of that attribute 'foundSub'
    foundSub = False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q : return True
        if not p and q : return False
        if p and not q : return False
        
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        if p.val == q.val and l and r: return True
        else: return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.foundSub: return True
        if not root and not subRoot:
            self.foundSub = True
            return True
        if root and not subRoot: return False
        if not root and subRoot: return False

        if self.isSameTree(root, subRoot): self.foundSub = True
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return self.foundSub