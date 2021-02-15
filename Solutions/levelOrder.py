# NAME : Binary Tree Level Order Traversal
# LINK : https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/
# DATE : 15/02/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level = [root] if root != None else []
        while level != []:
            next_level = []
            current_level = []
            while level != []:
                r = level.pop(0)
                current_level.append(r.val)
                if r.left != None:
                    next_level.append(r.left)
                if r.right != None:
                    next_level.append(r.right)
            level = next_level
            result.append(current_level)
        return result