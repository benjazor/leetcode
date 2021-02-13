# NAME : Symmetric Tree
# LINK : https://leetcode.com/problems/symmetric-tree/
# DATE : 13/02/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        return (
            root.left.val == root.right.val
            and self.isSymmetric(TreeNode(0, root.left.left, root.right.right))
            and self.isSymmetric(TreeNode(0, root.left.right, root.right.left))
        )
