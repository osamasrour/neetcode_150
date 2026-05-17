# Serialize and Deserialize Binary Tree: https://neetcode.io/problems/serialize-and-deserialize-binary-tree/question?list=neetcode150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    def find(self, lst, val):
        if val not in lst:
            return -1

        return lst.index(val)
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = self.find(inorder, preorder[0])
        if mid == -1:
            print(preorder[0])
            exit(-1)

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    def preOrderTrav(self, root) -> list[int]:
        res: list[Optional[int]]= []
        q = deque([root])
        while q:
            node = q.popleft()
            if node: 
                res.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res

    def inOrderTrav(self, root) -> list[int]:
        if not root: return []
        res = []
        def dfs(root):
            nonlocal res
            if not root: return None
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preOrder = self.preOrderTrav(root)
        inOrder = self.inOrderTrav(root)
        res: str = ""
        if not preOrder or not inOrder:
            return res
        for i in range(len(preOrder)):
            if i: res += ","
            res += str(preOrder[i])
        res += ";"
        for i in range(len(inOrder)):
            if i: res += ","
            res += str(inOrder[i])
        print(res)
        return res
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        _preOrder, _inOrder = data.split(";")
        _preOrder = _preOrder.split(",")
        _inOrder = _inOrder.split(",")
        print(_preOrder)
        preOrder = list(map(lambda x: int(x), _preOrder))
        inOrder = list(map(lambda x: int(x), _inOrder))
        print(preOrder)
        print(inOrder)
        root = self.buildTree(preOrder, inOrder)
        return root

"""
[1,2,3,null,null,4,5,null,null,null,null]
[0,1,2, 3,   4,  5,6]
l = i + 1
r = i + 2


"""