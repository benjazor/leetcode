# NAME : Binary Tree Zigzag Level Order Traversal
# LINK : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# DATE : 15/02/2021

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level = [root] if root else []
        zigzag = True
        while level != []:
            current_level = []
            next_level = []
            while level != []:
                node = level.pop(0)
                current_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
            result.append(current_level if zigzag else reversed(current_level))
            zigzag = not zigzag
        return result
