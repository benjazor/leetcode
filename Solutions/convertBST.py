# NAME : Convert BST to Greater Tree
# LINK : https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/
# DATE : 10/02/2021

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            dfs(root.left)

        dfs(root)
        return root


# https://en.wikipedia.org/wiki/Depth-first_search