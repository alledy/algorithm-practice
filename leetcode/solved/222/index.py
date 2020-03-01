# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        countl, countr = 1, 1
        leftChild, rightChild = root, root
        while leftChild.left:
            countl += 1
            leftChild = leftChild.left
        while rightChild.right:
            countr += 1
            rightChild = rightChild.right
        
        if countl == countr:
            return pow(2, countl) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        