# NAME : Minimum Distance Between BST Nodes
# LINK : https://leetcode.com/problems/minimum-distance-between-bst-nodes
# DATE : 03/05/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        def minDiffInBSTRec(root):
            if not root:
                return 10**5

            mini = min(
                # LEFT DISTANCE
                abs(root.val - (root.left.val if root.left else 10**5)),
                # RIGHT DISTANCE
                abs(root.val - (root.right.val if root.right else 10**5)),
                minDiffInBSTRec(root.left),
                minDiffInBSTRec(root.right),
            )

            next = root.left.right if root.left else None
            while next:
                if mini > root.val - next.val:
                    mini = root.val - next.val
                next = next.right

            next = root.right.left if root.right else None
            while next:
                if mini > next.val - root.val:
                    mini = next.val - root.val
                next = next.left

            return mini

        return minDiffInBSTRec(root)
