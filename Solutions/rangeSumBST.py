# NAME : Range Sum of BST
# LINK : https://leetcode.com/problems/range-sum-of-bst/submissions/
# DATE : 14/02/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        return (
            self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
            + (root.val if root.val <= high and root.val >= low else 0)
        )
