# NAME : Increasing Order Search Tree
# LINK : https://leetcode.com/problems/increasing-order-search-tree/
# DATE : 03/05/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def increasingBSTRec(root: TreeNode) -> TreeNode:
            if not root:
                return None

            if not root.left:
                return TreeNode(root.val, None, increasingBSTRec(root.right))

            result = increasingBSTRec(root.left)

            next = result
            while next.right:
                next = next.right

            next.right = TreeNode(
                root.val,
                None,
                increasingBSTRec(root.right)
            )
            return result

        return increasingBSTRec(root)
